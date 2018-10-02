# -*- coding:utf-8 -*-

# Standard library imports
from __future__ import unicode_literals


class BaseEntity(object):
    def hydrate(self, data):
        for k in data:
            if hasattr(self, k):
                setattr(self, k, data[k])
