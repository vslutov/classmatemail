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

import datetime
import imaplib
import smtplib
import time

try:
    import config
    if not config.READY_CONFIG:
        raise ImportError()
except ImportError as e:
    print("You haven't set config variables yet.")
    print("Please, view README file.")
    exit()


def updateMail():
    used = []
    sended = []

    with open('used.txt', 'r') as fout:
        used = fout.readline().split()
        fout.close()

    imap = imaplib.IMAP4_SSL(config.IMAP_SERVER)
    imap.login(config.MAILBOX_ADDRESS, config.MAILBOX_PASSWORD)
    imap.select('inbox')

    smtp = smtplib.SMTP_SSL(config.SMTP_SERVER)
    smtp.login(config.MAILBOX_ADDRESS, config.MAILBOX_PASSWORD)

    date = (datetime.date.today() - datetime.timedelta( \
            config.MAX_DAYS_AGO_LAST_RUN )).strftime("%d-%b-%Y")

    result, data = imap.uid('search', None, '(SENTSINCE {date})'\
                            .format(date=date))

    for uid in data[0].split():
        if used.count(str(uid)) == 0:
            result, data = imap.uid('fetch', uid, '(RFC822)')
            raw_email = data[0][1]
            smtp.sendmail(config.MAILBOX_ADDRESS, \
                          config.DISTRIBUTION_LIST, raw_email)
        sended.append(uid)

    imap.close()
    imap.logout()
    smtp.quit()

    sended = list(map(str, sended))
    with open('used.txt', 'w') as fout:
        fout.write(' '.join(sended))
        fout.close()


def update():
    try:
        updateMail()
    except Exception as e:
        with open('error.log', 'a') as eout:
            print(e, type(e))
            print(e, type(e), file=eout)
            eout.close()


while True:
    update()
    try:
        if config.RUN_ONCE:
            exit()
    except AttributeError:
        pass
    time.sleep( config.SECONDS_TO_NEXT_TRY )

