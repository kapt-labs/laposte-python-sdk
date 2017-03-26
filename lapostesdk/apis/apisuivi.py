from lapostesdk.apis.apibase import ApiBase

class ApiSuivi(ApiBase):
    def __init__(self, api_key):
        super(ApiSuivi, self).__init__(api_key, product='suivi')
