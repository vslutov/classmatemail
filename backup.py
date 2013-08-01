from __future__ import print_function

""" classmatemail - python-based e-mail broadcaster
    Copyright (C) 2013 V. S. Lutov

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as
    published by the Free Software Foundation, either version 3 of the
    License, or (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import imaplib

try:
    import config
    if not config.READY_CONFIG:
        raise ImportError()
except ImportError as e:
    print("You haven't set config variables yet.")
    print("Please, view README file.")
    exit()


class ReadingMailError(Exception):

    def __init__(self, result, data):
        self.str = (result, data)

    def __str__(self):
        return str(self.str)


with open('console.log', 'a') as logout:

    mail = imaplib.IMAP4_SSL(config.IMAP_SERVER)
    mail.login(config.MAILBOX_ADDRESS, config.MAILBOX_PASSWORD)
    mail.select('archivation')
 
    result, data = mail.uid('search', None, 'ALL')
    count = len(data[0].split())

    for uid in data[0].split():

        result, data = mail.uid('fetch', uid, '(RFC822)')
        
        if (result == 'OK') and (type(data) is list)\
           and (data[1] == ')') and (type(data[0]) is tuple):

            with open(uid + '.eml', 'w') as fout:
                raw_email = data[0][1]
                print(raw_email, file=fout)
                print('OK', uid, 'from', count)
                fout.close()

        else:
            raise ReadingMailError(result, data)

    mail.close()
    mail.logout()
    logout.close()
