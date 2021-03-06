# Copyright (C) 2015 Sebastian Herbord.  All rights reserved.
# Copyright (C) 2016 - 2018 Mod Organizer contributors.
#
# This file is part of Mod Organizer.
#
# Mod Organizer is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Mod Organizer is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Mod Organizer.  If not, see <http://www.gnu.org/licenses/>.
from contextlib import contextmanager


@contextmanager
def on_failure(func):
    """
    very generic context object generator that will run a parameterless lambda in case the
    wrapped code fails
    """
    try:
        yield
    except:
        func()
        raise


@contextmanager
def on_exit(func):
    """
    very generic context object generator that will run a parameterless lambda in case the
    wrapped code fails
    """
    try:
        yield
        func()
    except:
        func()
        raise
