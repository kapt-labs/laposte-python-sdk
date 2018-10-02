# -*- coding:utf-8 -*-

# Standard library imports
from __future__ import unicode_literals

from lapostesdk.entities.base import BaseEntity


class TarifEnvoi(BaseEntity):
    def __init__(self):
        self.channel = None
        self.currency = None
        self.price = None
        self.product = None
