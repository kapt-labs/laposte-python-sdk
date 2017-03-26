import requests

class ApiBase(object):
    def __init__(self, api_key, product, version='v1'):
        self.product = product
        self.version = version

        self.api_url = 'https://api.laposte.fr/%(product)s/%(version)s/' % {
                'product': self.product,
                'version': self.version}

        self.headers = {'X-Okapi-Key': api_key}

    def get(self, resource, params={}):
        r = requests.get(self.api_url + resource, params=params, headers=self.headers)
        return r.json()
