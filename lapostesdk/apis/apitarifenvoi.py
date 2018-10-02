# -*- coding:utf-8 -*-

# Standard library imports
from __future__ import unicode_literals

from lapostesdk.apis.apibase import ApiBase


class ApiTarifEnvoi(ApiBase):
    def __init__(self, api_key):
        super(ApiTarifEnvoi, self).__init__(api_key, product='tarifenvoi', entity='TarifEnvoi')

    def get(self, type, weight, channels=[], products=[]):
        params = {'type': type,
                  'poids': weight}

        response = self._get('', params)
        response_objects = [self.create_object(r, self.entity) for r in response]

        if len(channels) > 0:
            response_objects = [response_object for response_object in response_objects if response_object.channel in [channel.value for channel in channels]]

        if len(products) > 0:
            response_objects = [response_object for response_object in response_objects if response_object.product in [product.value for product in products]]

        return response_objects
