from __future__ import print_function

"""
    classmatemail - python-based e-mail broadcaster
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

### [BEGIN] Configuration section ###

IMAP_SERVER = 'imap.example.com'
SMTP_SERVER = 'smtp.example.com'

MAILBOX_ADDRESS = 'classmates@example.com'
MAILBOX_PASSWORD = 'correctHorseBatteryStaple'

DISTRIBUTION_LIST = ['a@example.com', 'b@example.com', 'c@example.com']

MAX_DAYS_AGO_LAST_RUN = 5
SECONDS_TO_NEXT_TRY = 60 * 5

###  [END]  Configuration section ###

import datetime, imaplib, smtplib, time

def updateMail():
    used = []
    sended = []

    with open('used.txt', 'r') as fout:
        used = fout.readline().split()
        fout.close()
        
    mail = imaplib.IMAP4_SSL(IMAP_SERVER)
    mail.login(MAILBOX_ADDRESS, MAILBOX_PASSWORD)
    mail.list()
    mail.select('inbox')

    send = smtplib.SMTP_SSL(SMTP_SERVER)
    send.login(MAILBOX_ADDRESS, MAILBOX_PASSWORD)
 
    date = (datetime.date.today() - datetime.timedelta( MAX_DAYS_AGO_LAST_RUN )).strftime("%d-%b-%Y")
    result, data = mail.uid('search', None, '(SENTSINCE {date})'.format(date=date))

    for uid in data[0].split():
        if used.count(str(uid)) == 0:
            result, data = mail.uid('fetch', uid, '(RFC822)')
            raw_email = data[0][1]
            send.sendmail(MAILBOX_ADDRESS, DISTRIBUTION_LIST, raw_email)
        sended.append(uid)

    mail.close()
    mail.logout()
    send.quit()
        
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
    time.sleep( SECONDS_TO_NEXT_TRY )
