#!/bin/sh

cd /tmp

rm -rf test-project*

quickly create ubuntu-application test-project
# Creating bzr repository and committing
# Congrats, your new project is setup! cd /tmp/test-project/ to start hacking.
# Creating project directory test-project

cd test-project

quickly license
# Copyright is not attributed. Edit the AUTHORS file to include your name for the copyright replacing <Your Name> <Your E-mail>. Update it in setup.py or use quickly share/quickly release to fill it automatically
# ERROR: license command failed
# Aborting

quickly license GPL-2 GPL-3
# ERROR: This command only take one optional argument.
# Usage: quickly license [license-name]
# Candidate licenses: Apache-2.0, BSD, GPL-2, GPL-3, LGPL-2, LGPL-3, MIT, other

quickly license GPL-0
# ERROR: Unknown licence GPL-0.
# Usage: quickly license [license-name]
# Candidate licenses: Apache-2.0, BSD, GPL-2, GPL-3, LGPL-2, LGPL-3, MIT, other

(echo "Copyright (C) 2010 Oliver Twist <twist@example.com>" > AUTHORS)

(echo "This file is licensed under the OTL (Oliver Twist License)" > COPYING)

quickly license
# COPYING contains an unknown license.  Please run 'quickly license other' to confirm that you want to use a custom license.
# ERROR: license command failed
# Aborting

quickly license other

grep license= setup.py
#     license='other',

grep "Oliver Twist License" setup.py
# # This file is licensed under the OTL (Oliver Twist License)

cat COPYING
# This file is licensed under the OTL (Oliver Twist License)

sed -i "s/license=.*,/#license='other',/" setup.py

cp /usr/share/common-licenses/BSD COPYING

quickly license

diff -q /usr/share/common-licenses/BSD COPYING

grep license= setup.py
#     license='BSD',

grep "The Regents of the University of California" setup.py
# # Copyright (c) The Regents of the University of California.

sed -i "s/license=.*,/license='GPL-2',/" setup.py

quickly license

grep license= setup.py
#     license='GPL-2',

grep "General Public License version" setup.py
# # under the terms of the GNU General Public License version 2, as published 

grep -A 1 -m 1 "GENERAL PUBLIC LICENSE" COPYING
#                     GNU GENERAL PUBLIC LICENSE
#                        Version 2, June 1991

quickly license GPL-3

grep license= setup.py
#     license='GPL-3',

grep "General Public License version" setup.py
# # under the terms of the GNU General Public License version 3, as published 

grep -A 1 -m 1 "GENERAL PUBLIC LICENSE" COPYING
#                     GNU GENERAL PUBLIC LICENSE
#                        Version 3, 29 June 2007
