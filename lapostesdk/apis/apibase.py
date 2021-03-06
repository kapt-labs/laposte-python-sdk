# -*- coding:utf-8 -*-

# Standard library imports
from __future__ import unicode_literals

import requests
from importlib import import_module


class ApiBase(object):
    def __init__(self, api_key, product, version='v1', entity=None):
        self.product = product
        self.version = version
        self.entity = entity

        self.api_url = 'https://api.laposte.fr/%(product)s/%(version)s/' % {
                       'product': self.product,
                       'version': self.version}

        self.headers = {'X-Okapi-Key': api_key}

    def get(self, resource, params={}):
        response = self._get(resource, params)
        if self.entity is None:
            return response

        return self.create_object(response, self.entity)

    def _get(self, resource, params={}):
        response = requests.get(self.api_url + resource, params=params, headers=self.headers)

        status_code = response.status_code
        content = response.json()

        if status_code != 200:
            raise Exception(content['message'])

        return content

    def create_object(self, response, entity):
        module = import_module('lapostesdk.entities')
        obj = getattr(module, self.entity)
        instance = obj()
        instance.hydrate(response)
        return instance
