# -*- Mode:Python; indent-tabs-mode:nil; tab-width:4 -*-
#
# Copyright 2023 Canonical Ltd.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 3 as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""Extension processor and related utilities."""

from ._utils import apply_extensions
from .app_parts import gen_logging_part
from .expressjs import ExpressJSFramework
from .fastapi import FastAPIFramework
from .go import GoFramework
from .gunicorn import DjangoFramework, FlaskFramework
from .registry import get_extension_class, get_extension_names, register, unregister
from .springboot import SpringBootFramework

__all__ = [
    "get_extension_class",
    "get_extension_names",
    "apply_extensions",
    "register",
    "unregister",
    "gen_logging_part",
]

register("django-framework", DjangoFramework)
register("expressjs-framework", ExpressJSFramework)
register("fastapi-framework", FastAPIFramework)
register("flask-framework", FlaskFramework)
register("go-framework", GoFramework)
register("spring-boot-framework", SpringBootFramework)
