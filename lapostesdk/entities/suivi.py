# -*- coding:utf-8 -*-

# Standard library imports
from __future__ import unicode_literals

from lapostesdk.entities.base import BaseEntity


class Suivi(BaseEntity):
    def __init__(self):
        self.code = None
        self.date = None
        self.status = None
        self.message = None
        self.link = None
        self.type = None
