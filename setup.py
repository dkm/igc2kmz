#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#   IGC to Google Earth converter
#   Copyright (C) 2009  Marc Poulhiès
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.


from distutils.core import setup

setup (
    name = "igc2kmz",
    description = "IGC to Google Earth converter",
    long_description = """
This package provides a python module for handling kmz files. It
also comes with frontend scripts
""",
    version = "0.2",
    author = 'Tom Payne',
    author_email = 'twpayne@gmail.com',
    url = "http://github.com/twpayne/igc2kmz",
    maintainer = 'Marc Poulhiès',
    maintainer_email = 'dkm@kataplop.net',
    license = "GPL",
    packages = ['igc2kmz', 'igc2kmz.third_party'],
    scripts=['bin/%s' %i for i in ["brand2kml.py", 
                                   "igc2kmz.py", 
                                   "igc2task.py", 
                                   "leonardo2kmz.py", 
                                   "olc2gpx.py"]],
    package_data={'igc2kmz': ['images/*']},
    )

