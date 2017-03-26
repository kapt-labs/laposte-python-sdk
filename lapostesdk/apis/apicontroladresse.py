from lapostesdk.apis.apibase import ApiBase

class ApiControlAdresse(ApiBase):
    def __init__(self, api_key):
        super(ApiControlAdresse, self).__init__(api_key, product='controladresse')

    def search(self, address):
        payload = {'q': address}
        return self.get('adresses', params=payload)
