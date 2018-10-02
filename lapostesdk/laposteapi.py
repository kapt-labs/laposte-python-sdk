# -*- coding:utf-8 -*-

# Standard library imports
from __future__ import unicode_literals

from lapostesdk.apis import apisuivi, apicontroladresse, apitarifenvoi


class LaPosteApi(object):
    def __init__(self, api_key):
        self.api_key = api_key

        self.suivi = apisuivi.ApiSuivi(self.api_key)
        self.controladresse = apicontroladresse.ApiControlAdresse(self.api_key)
        self.tarifenvoi = apitarifenvoi.ApiTarifEnvoi(self.api_key)
