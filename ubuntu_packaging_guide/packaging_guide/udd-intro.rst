==============================
Ubuntu Distributed Development
==============================

*Ubuntu Distributed Development* (UDD) is a technique for developing Ubuntu
packages that uses tools, processes, and workflows similar to generic
distributed version control (dVCS) system-based software development.  The
dVCS used for UDD is Bazaar_.

You should already be familiar with basic Bazaar usage and workflow.  Ubuntu
Intrepid_ or later is required for these instructions to work.


Source package URLs
===================

Bazaar provides some very nice shortcuts for accessing the source branches of
packages in both Ubuntu and Debian (on Launchpad).  These shortcuts are
available in Bazaar version 2.3 or newer.  You can still access source
branches in older versions of Bazaar, using a slightly more verbose syntax.

The examples in this guide always use the ``ubuntu:`` prefix.


Source branch shortcuts
-----------------------

To refer to source branches use::

    ubuntu:package

where *package* refers to the package name you're interested in.  This URL
refers to the package in the current development version of Ubuntu.  As of
this writing (2011-02-04) that version is Natty_ which will be released as
Ubuntu 11.04.  Thus, to refer to the branch of Tomboy in Natty, you would
use::

    ubuntu:tomboy

To refer to the version of a source package in an older release of ubuntu,
just prefix the package name with the release's code name.  E.g. to refer to
Tomboy's source package in Maverick_ use::

    ubuntu:maverick/tomboy

Since they are unique, you can also abbreviate the distro-series name::

    ubuntu:m/tomboy

You can use a similar scheme to access the source branches in Debian, although
there are no shortcuts for the Debian distro-series names.  To access the
Tomboy branch in the current development series for Debian use:

    debianlp:tomboy

and to access Tomboy in Debian Lenny_ use::

    debianlp:lenny/tomboy


Explicit source branches
------------------------

If you're using an older version of Bazaar, the ``ubuntu:`` and ``debianlp:``
prefixes won't be available to you.  Instead use the ``lp:`` prefix to access
the source branch.  For example, Tomboy in the latest Ubuntu development
release is available at::

    lp:ubuntu/tomboy

while the Maverick version is available at::

    lp:ubuntu/maverick/tomboy

and the Debian Lenny version is available at::

    lp:debian/lenny/tomboy


.. _`Bazaar`: http://bazaar.canonical.com/en/
.. _`Intrepid`: https://wiki.ubuntu.com/IntrepidIbex
.. _Natty: https://wiki.ubuntu.com/NattyNarwhal
.. _Maverick: https://wiki.ubuntu.com/MaverickMeerkat
.. _Lenny: http://debian.org/releases/stable/


Getting the source
==================

Every source package in Ubuntu has an associated source branch on Launchpad.
These source branches are updated automatically by Launchpad, although the
process is not currently foolproof.

There are a couple of things that we do first in order to make the workflow
more efficient later.  Once you are used to the process you will learn when it
makes sense to skip these steps.


.. _up-to-date:

Ensure the source branch is up-to-date
--------------------------------------

Once you've determined which source package to work on, you should ensure that
the source branch for that package on Launchpad is up-to-date.  Some package
imports fail for various reasons, and the `status of the package importer`_ is
always available online.  If the source branch for a package you want to work
on is out of sync, you'll have to use ``apt-get source`` until the import of
that package is fixed.

Let's say you want to fix a problem in Tomboy in Natty.  First, find out the
latest binary package versions that are available::

    $ rmadison tomboy | grep natty
    tomboy | 1.5.2-1ubuntu4 |         natty | source, amd64, i386

You've already seen how to :ref:`determine the source package corresponding to
this binary package <what-to-fix>`.  For Tomboy, the binary and source
packages are both named ``tomboy``.

Whenever the package importer processes a new source package version, it adds
a Bazaar tag corresponding to that new version.  You can use this tag to
ensure that the import is up-to-date.  To find the tag of the last revision
committed by the package importer, do::

    $ bzr log -l 1 ubuntu:tomboy | grep ^tags:
    tags: 1.5.2-1ubuntu4

By comparing the version number returned by ``rmadison`` and the tag added by
the package importer, we can see that the ``tomboy`` source package for Natty
is up-to-date.

Here's an example of a package that is out-of-date.  Let's say you want to fix
a problem in the ``initscripts`` binary package on Natty_.  First find out the
latest binary package versions that are available::

    $ rmadison initscripts | grep natty
    initscripts | 2.87dsf-4ubuntu19 |         natty | amd64, i386

Then determine the source package corresponding to this binary package::

    $ apt-cache show initscripts | grep ^Source:
    Source: sysvinit

Find the latest tag added by the package importer::

    $ bzr log -l 1 ubuntu:sysvinit | grep ^tags:
    tags: 2.86.ds1-61ubuntu13

Here we can see that ``2.86.ds1-61ubuntu13`` is older than
``2.87dsf-4ubuntu19`` so the source package is out of date, and in fact we can
verify that by looking at the status package for the package at
http://package-import.ubuntu.com/status/sysvinit.html.

When you find such out-of-date packages, be sure to `file a bug on the UDD
project`_ to get the issue resolved.

.. _branching:

Creating a shared repository
----------------------------

Okay, you want to work on the Tomboy package in Natty, and you've verified
that the source package is up-to-date.  Before actually branching the code for
Tomboy, create a shared repository to hold the branches for this package.
The shared repository will make future work much more efficient.

Do this using the `bzr init-repo` command, passing it the directory name we
would like to use::

    $ bzr init-repo tomboy

You will see that a `tomboy` directory is created in your current working
area.  Change to this new directory for the rest of your work::

    $ cd foobar


Getting the trunk branch
------------------------

We use the `bzr branch` command to create a local branch of the package.
We'll name the target directory `natty` just to keep things easy to remember::

    $ bzr branch ubuntu:tomboy natty

The `natty` directory represents the version of Tomboy in Natty, and you can
always ``cd`` into this directory and do a `bzr pull` to get any future
updates.


Getting a branch for a particular release
-----------------------------------------

When you want to do something like a `stable release update`_ (SRU), or you
just want to examine the code in an old release, you'll want to grab the
branch corresponding to a particular Ubuntu release.  For example, to get the
Tomboy package for Maverick do::

    $ bzr branch ubuntu:m/tomboy maverick


Importing a Debian source package
---------------------------------

If the package you want to work on is available in Debian but not Ubuntu, it's
still easy to import the code to a local bzr branch for development.  Let's
say you want to import the `newpackage` source package.  We'll start by
creating a shared repository as normal, but we also have to create a working
tree to which the source package will be imported (remember to cd out of the
`tomboy` directory created above)::

    $ bzr init-repo newpackage
    $ cd new-package
    $ bzr init debian
    $ cd debian
    $ bzr import-dsc http://ftp.de.debian.org/debian/pool/main/n/newpackage/newpackage_1.0-1.dsc

As you can see, we just need to provide the remote location of the dsc file,
and Bazaar will do the rest.  You've now got a Bazaar source branch.


.. _`status of the package importer`: http://package-import.ubuntu.com/status
.. _`file a bug on the UDD project`: https://bugs.launchpad.net/udd
.. _`stable release update`: https://wiki.ubuntu.com/StableReleaseUpdates
