#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Isomer - The distributed application framework
# ==============================================
# Copyright (C) 2011-2019 Heiko 'riot' Weinen <riot@c-base.org> and others.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

__author__ = "Heiko 'riot' Weinen"
__license__ = "AGPLv3"

from setuptools import setup, find_packages

setup(
    name="isomer-calendar",
    version="0.0.1",
    description="isomer-calendar",

    author="Isomer Community",
    author_email="riot@c-base.org",
    url="https://github.com/isomeric/isomer-calendar",
    license="GNU Affero General Public License v3",
    namespace_packages=['isomer'],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Web Environment',
        'Framework :: Isomer :: 1',
        'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
        'Operating System :: Linux',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Office/Business :: Scheduling'
    ],
    packages=find_packages(),
    include_package_data=True,
    long_description="""Isomer - Calendar
=================

Calendar resource management module.

This software package is a plugin module for Isomer.
""",
    dependency_links=[],
    install_requires=[
        'isomer>=1.0',
        'icalendar>=4.0.1'
    ],
    entry_points="""[isomer.components]
    calendar=isomer.calendar.calendarmanager:CalendarManager
    [isomer.schemata]
    event=isomer.calendar.event:Event
    calendar=isomer.calendar.calendar:Calendar
    [isomer.management]
    icalimporter=isomer.calendar.importer.ical:ICALImporter
    """,
    test_suite="tests.main.main",
)
