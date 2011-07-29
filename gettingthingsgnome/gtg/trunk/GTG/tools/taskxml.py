# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Gettings Things Gnome! - a personal organizer for the GNOME desktop
# Copyright (c) 2008-2009 - Lionel Dricot & Bertrand Rousseau
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

#Functions to convert a Task object to an XML string and back
import xml.dom.minidom
import xml.sax.saxutils as saxutils
import datetime

from GTG.tools import cleanxml
from GTG.tools import dates

#Take an empty task, an XML node and return a Task.
def task_from_xml(task,xmlnode) :
    cur_task = task
    cur_stat = "%s" %xmlnode.getAttribute("status")
    uuid = "%s" %xmlnode.getAttribute("uuid")
    cur_task.set_uuid(uuid)
    donedate = cleanxml.readTextNode(xmlnode,"donedate")
    cur_task.set_status(cur_stat,donedate=dates.strtodate(donedate))
    #we will fill the task with its content
    cur_task.set_title(cleanxml.readTextNode(xmlnode,"title"))
    #the subtasks
    sub_list = xmlnode.getElementsByTagName("subtask")
    for s in sub_list :
        sub_tid = s.childNodes[0].nodeValue
        cur_task.add_child(sub_tid)
    attr_list = xmlnode.getElementsByTagName("attribute")
    for a in attr_list:
        if len(a.childNodes):
            content = a.childNodes[0].nodeValue
        else:
            content = ""
        key = a.getAttribute("key")
        namespace = a.getAttribute("namespace")
        cur_task.set_attribute(key, content, namespace=namespace)
    tasktext = xmlnode.getElementsByTagName("content")
    if len(tasktext) > 0 :
        if tasktext[0].firstChild :
            tas = "<content>%s</content>" %tasktext[0].firstChild.nodeValue
            content = xml.dom.minidom.parseString(tas)
            cur_task.set_text(content.firstChild.toxml()) #pylint: disable-msg=E1103 
    cur_task.set_due_date(dates.strtodate(cleanxml.readTextNode(xmlnode,"duedate")))
    cur_task.set_start_date(dates.strtodate(cleanxml.readTextNode(xmlnode,"startdate")))
    cur_tags = xmlnode.getAttribute("tags").replace(' ','').split(",")
    if "" in cur_tags: cur_tags.remove("")
    for tag in cur_tags: cur_task.tag_added(saxutils.unescape(tag))

    #REMOTE TASK IDS
    remote_ids_list = xmlnode.getElementsByTagName("task-remote-ids")
    for remote_id in remote_ids_list:
        if remote_id.childNodes:
            node = remote_id.childNodes[0]
            backend_id = node.firstChild.nodeValue
            remote_task_id = node.childNodes[1].firstChild.nodeValue
            task.add_remote_id(backend_id, remote_task_id)
    modified_string = cleanxml.readTextNode(xmlnode,"modified")
    if modified_string:
        modified_datetime = datetime.datetime.strptime(modified_string,\
                                                    "%Y-%m-%dT%H:%M:%S")
        cur_task.set_modified(modified_datetime)
    return cur_task

#Task as parameter the doc where to put the XML node
def task_to_xml(doc,task) :
    t_xml = doc.createElement("task")
    t_xml.setAttribute("id",task.get_id())
    t_xml.setAttribute("status" , task.get_status())
    t_xml.setAttribute("uuid" , task.get_uuid())
    tags_str = ""
    for tag in task.get_tags_name(): 
        tags_str = tags_str + saxutils.escape(str(tag)) + ","
    t_xml.setAttribute("tags", tags_str[:-1])
    cleanxml.addTextNode(doc,t_xml,"title",task.get_title())
    cleanxml.addTextNode(doc,t_xml,"duedate", task.get_due_date().xml_str())
    cleanxml.addTextNode(doc,t_xml,"modified",task.get_modified_string())
    cleanxml.addTextNode(doc,t_xml,"startdate", task.get_start_date().xml_str())
    cleanxml.addTextNode(doc,t_xml,"donedate", task.get_closed_date().xml_str())
    childs = task.get_children()
    for c in childs :
        cleanxml.addTextNode(doc,t_xml,"subtask",c)
    for a in task.attributes:
        namespace,key=a
        content=task.attributes[a]
        element = doc.createElement('attribute')
        element.setAttribute("namespace", namespace)
        element.setAttribute("key", key)
        element.appendChild(doc.createTextNode(content))
        t_xml.appendChild(element)
    tex = task.get_text()
    if tex :
        #We take the xml text and convert it to a string
        #but without the "<content />" 
        element = xml.dom.minidom.parseString(tex)
        temp = element.firstChild.toxml().partition("<content>")[2] #pylint: disable-msg=E1103
        desc = temp.partition("</content>")[0]
        #t_xml.appendChild(element.firstChild)
        cleanxml.addTextNode(doc,t_xml,"content",desc)
    #self.__write_textnode(doc,t_xml,"content",t.get_text())

    #REMOTE TASK IDS
    remote_ids_element = doc.createElement("task-remote-ids")
    t_xml.appendChild(remote_ids_element)
    remote_ids_dict = task.get_remote_ids()
    for backend_id, task_id in remote_ids_dict.iteritems():
        backend_element = doc.createElement('backend')
        remote_ids_element.appendChild(backend_element)
        backend_element.appendChild(doc.createTextNode(backend_id))
        task_element = doc.createElement('task-id')
        backend_element.appendChild(task_element)
        task_element.appendChild(doc.createTextNode(task_id))


    return t_xml
