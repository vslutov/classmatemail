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

IMAP_SERVER = 'imap.example.com'
SMTP_SERVER = 'smtp.example.com'

MAILBOX_ADDRESS = 'classmates@example.com'
MAILBOX_PASSWORD = 'correctHorseBatteryStaple'

DISTRIBUTION_LIST = ['a@example.com', 'b@example.com', 'c@example.com']

MAX_DAYS_AGO_LAST_RUN = 5

RUN_ONCE = False
SECONDS_TO_NEXT_TRY = 60 * 5 # If RUN_ONCE is False

READY_CONFIG = False
