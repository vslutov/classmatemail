# classmatemail

[Official site](https://github.com/vslutov/classmatemail)

## License

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

## Description

If you need only broadcast mail to many destinations, you may use this script.

## Requirements

Python 2 or Python 3.

You can download it there: <http://www.python.org/download/>

## How-to...

### configure

1. Rename `config.sample.py` into `config.py`
2. Edit renamed file
3. Don't forget set `READY_CONFIG` variable into `True`

### start

1. Make sure, that your computer have right system time setting.
2. [Configure](#configure)
3. Write start script, like

        cd %ABSOLUTE_PATH_TO_LOCAL_DIRECTORY_WITH_SCRIPT%
        python main.py

4. Add start script to autorun

(Add shortcut to `start.bat` to 
`C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup` in windows.)

### backup

1. [Configure](#configure)
2. Enter console and run

        python backup.py
