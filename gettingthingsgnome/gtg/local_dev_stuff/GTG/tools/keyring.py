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

import gnomekeyring

from GTG.tools.borg import Borg



class Keyring(Borg):


    def __init__(self):
        super(Keyring, self).__init__()
        if not hasattr(self, "keyring"):
            self.keyring = gnomekeyring.get_default_keyring_sync()

    def set_password(self, name, password, userid = ""):
        return gnomekeyring.item_create_sync(
                    self.keyring,
                    gnomekeyring.ITEM_GENERIC_SECRET,
                    name,
                    {"backend": name},
                    password,
                    True)

    def get_password(self, item_id):
        try:
            item_info = gnomekeyring.item_get_info_sync(self.keyring, item_id)
            return item_info.get_secret()
        except (gnomekeyring.DeniedError, gnomekeyring.NoMatchError):
            return ""
