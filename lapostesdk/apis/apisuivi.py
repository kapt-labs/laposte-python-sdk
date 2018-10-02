# -*- coding:utf-8 -*-

# Standard library imports
from __future__ import unicode_literals

from lapostesdk.apis.apibase import ApiBase


class ApiSuivi(ApiBase):
    def __init__(self, api_key):
        super(ApiSuivi, self).__init__(api_key, product='suivi', entity='Suivi')
