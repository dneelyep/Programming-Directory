# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Getting Things Gnome! - a personal organizer for the GNOME desktop
# Copyright (c) 2008-2010 - Lionel Dricot & Bertrand Rousseau
#
# This program is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# this program.  If not, see <http://www.gnu.org/licenses/>.
# -----------------------------------------------------------------------------

#If True, the TreeTester will automatically reorder node on the same level
#as a deleted node. If False, it means that Liblarch has the responsability
#to handle that itself.
REORDER_ON_DELETE = False

class TreeTester:
    '''A class that will check if a tree implementation is consistent
    by connecting to emitted signals and crashing on any problem'''
    def __init__(self,viewtree):
        self.tree = viewtree
        #both dict should always be synchronized
        #They are the internal representation of the tree,
        #based only on received signals
        self.nodes = {}
        self.paths = {}
        self.tree.register_cllbck('node-added-inview',self.add)
        self.tree.register_cllbck('node-deleted-inview',self.delete)
        self.tree.register_cllbck('node-modified-inview',self.update)
        self.tree.register_cllbck('node-children-reordered',self.reordered)
        self.trace = "* * * * * * * *\n"
        self.state_id = 0
        
        
    def add(self,nid,path,state_id):
        self.state_id = state_id
        self.trace += "adding %s to path %s\n" %(nid,str(path))
        print "adding %s to path %s" %(nid,str(path))
        currentnode = self.paths.get(path,None)
        if currentnode and currentnode != nid:
            raise Exception('path %s is already occupied by %s' %(str(path),nid))
        if self.nodes.has_key(nid):
            node = self.nodes[nid]
        else:
            node = []
            self.nodes[nid] = node
        if path not in node:
            node.append(path)
        self.paths[path] = nid
    
    def delete(self,nid,path,state_id):
        self.state_id = state_id
        self.trace += "removing %s from path %s\n" %(nid,str(path))
        print "removing %s from path %s" %(nid,str(path))
        if nid != self.paths.get(path,None):
            error = '%s is not assigned to path %s\n'%(nid,str(path))
            error += self.print_tree()
            raise Exception(error)
        if path not in self.nodes.get(nid,[]):
            raise Exception('%s is not a path of node %s'%(str(path),nid))
        if REORDER_ON_DELETE:
            index = path[-1:]
            print "reorder on delete not yet implemented"
        self.nodes[nid].remove(path)
        if len(self.nodes[nid]) == 0:
            self.nodes.pop(nid)
        self.paths.pop(path)
    
    def update(self,nid,path,state_id):
        self.state_id = state_id
        self.trace += "updating %s in path %s\n" %(nid,str(path))
        error = "updating node %s for path %s\n" %(nid,str(path))
        if not self.nodes.has_key(nid):
            error += "%s is not in nodes !\n" %nid
            error += self.print_tree()
            raise Exception(error)
        #Nothing to do, we just update.
        for p in self.nodes[nid]:
            if self.paths[p] != nid:
                raise Exception('Mismatching path for %s'%nid)
        if not self.paths.has_key(path):
            error += '%s is not in stored paths (node %s)\n'%(str(path),nid)
            error += self.print_tree()
            raise Exception(error)
        n = self.paths[path]
        if path not in self.nodes[n] or n != nid:
            raise Exception('Mismatching node for path %s'%str(p))
            
    def reordered(self,nid,path,neworder,state_id):
        print "reordering"
        self.state_id = state_id
        self.trace += "reordering children of %s (%s) : %s\n" %(nid,str(path),neworder)
        self.trace += "VR is %s\n" %self.tree.node_all_children()
        if not path:
            path = ()
        i = 0
        newpaths = {}
        toremove = []
        #we first update self.nodes with the new paths
        while i < len(neworder):
            if i != neworder[i]:
                old = neworder[i]
                oldp = path + (old,)
                newp = path + (i,)
                le = len(newp)
                for pp in self.paths.keys():
                    if pp[0:le] == oldp:
                        n = self.paths[pp]
                        self.nodes[n].remove(pp)
                        newpp = newp + pp[le:]
                        self.nodes[n].append(newpp)
                        self.trace += "    change %s path from %s to %s\n" %(n,pp,newpp)
                        newpaths[newpp] = n
                        toremove.append(pp)
            i += 1
        #now we can update self.paths
        for p in toremove:
            self.paths.pop(p)
        for p in newpaths:
            self.trace += "    adding %s to paths %s\n" %(newpaths[p],str(p))
            self.paths[p] = newpaths[p]
            
    
    
    def test_validity(self):
        for n in self.nodes.keys():
            paths = self.tree.get_paths_for_node(n,state_id=self.state_id)
            if len(self.nodes[n]) == 0:
                raise Exception('Node %s is stored without any path'%n)
            for p in self.nodes[n]:
                if self.paths[p] != n:
                    raise Exception('Mismatching path for %s'%n)
                if p not in paths:
                    error = 'we have a unknown stored path for %s\n' %n
                    nn = self.tree.get_node_for_path(p)
                    error += '  path %s is the path of %s\n' %(str(p),str(nn))
                    error += '  parent is %s' %self.tree.get_node_for_path(p[:-1])
#                    error += self.trace
                    raise Exception(error)
                paths.remove(p)
            if len(paths) > 0:
                raise Exception('why is this path existing for %s' %n)
        for p in self.paths.keys():
            node = self.tree.get_node_for_path(p,state_id=self.state_id)
            n = self.paths[p]
            if n != node:
                error = 'Node for path is %s but should be %s' %(node,n)
                raise Exception(error)
            if p not in self.nodes[n]:
                error = 'Mismatching node for path %s\n'%str(p)
                error += self.print_tree()
                raise Exception(error)
            if len(p) == 1 and len(self.nodes[n]) > 1:
                error = 'Node %s has multiple paths and is in the VR\n' %n
                error += self.print_tree()
                raise Exception(error)
        return True
        
    def print_tree(self):
        st = self.trace
        st += "nodes are %s\n" %self.nodes
        st += "paths are %s\n" %self.paths
        return st

    def quit(self):
        self.tree.deregister_cllbck('node-added-inview',self.add)
        self.tree.deregister_cllbck('node-deleted-inview',self.delete)
        self.tree.deregister_cllbck('node-modified-inview',self.update)
        self.tree.deregister_cllbck('node-children-reordered',self.reordered)
