#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest
import responses

from lapostesdk.laposteapi import LaPosteApi
from lapostesdk.constants.tarifenvoi import TarifEnvoiChannels
from lapostesdk.constants.tarifenvoi import TarifEnvoiProducts


class TestBase(unittest.TestCase):
    def setUp(self):
        self.api = LaPosteApi('TheApiKey')


class TestSuiviApi(TestBase):
    @responses.activate
    def test_get(self):
        responses.add(responses.GET,
                      'https://api.laposte.fr/suivi/v1/1111111111111',
                      json={'code': '1111111111111'}, status=200)

        r = self.api.suivi.get('1111111111111')
        self.assertEqual("1111111111111", r.code)

        self.assertEquals(len(responses.calls), 1)
        self.assertEquals(responses.calls[0].request.url, 'https://api.laposte.fr/suivi/v1/1111111111111')
        self.assertEquals(responses.calls[0].request.headers['X-Okapi-Key'], 'TheApiKey')

    @responses.activate
    def test_bad_request(self):
        responses.add(responses.GET,
                      'https://api.laposte.fr/suivi/v1/123',
                      json={'code': 'BAD_REQUEST', 'message': 'Mauvais format pour le paramètre code'}, status=400)

        with self.assertRaises(Exception):
            self.api.suivi.get('123')

    @responses.activate
    def test_resource_not_found(self):
        responses.add(responses.GET,
                      'https://api.laposte.fr/suivi/v1/1111111111119',
                      json={'code': 'RESOURCE_NOT_FOUND', 'message': 'Aucun produit ne correspond à votre recherche'}, status=404)

        with self.assertRaises(Exception):
            self.api.suivi.get('1111111111119')


class TestControlAdresseApi(TestBase):
    @responses.activate
    def test_search(self):
        responses.add(responses.GET,
                      'https://api.laposte.fr/controladresse/v1/adresses',
                      json=[{'foo': 'bar'}], status=200)

        r = self.api.controladresse.search('116 avenue du Président Kennedy 75220 Paris Cedex 16')
        self.assertEqual("bar", r[0]['foo'])

        self.assertEquals(len(responses.calls), 1)
        #self.assertEquals(responses.calls[0].request.url, 'https://api.laposte.fr/controladresse/v1/adresses')
        #self.assertEquals(responses.calls[0].request.params, {'q': '116 avenue du Président Kennedy 75220 Paris Cedex 16'})
        self.assertEquals(responses.calls[0].request.headers['X-Okapi-Key'], 'TheApiKey')

    @responses.activate
    def test_get(self):
        responses.add(responses.GET,
                      'https://api.laposte.fr/controladresse/v1/plop',
                      json={'codePostal': 'bar'}, status=200)

        r = self.api.controladresse.get('plop')
        self.assertEqual("bar", r.codePostal)

        self.assertEquals(len(responses.calls), 1)
        self.assertEquals(responses.calls[0].request.url, 'https://api.laposte.fr/controladresse/v1/plop')
        self.assertEquals(responses.calls[0].request.headers['X-Okapi-Key'], 'TheApiKey')


class TestTarifEnvoiApi(TestBase):
    @responses.activate
    def test_get(self):
        responses.add(responses.GET,
                      'https://api.laposte.fr/tarifenvoi/v1/',
                      json=[{'currency': '€', 'product': 'Lettre verte', 'price': 0.8, 'channel': 'bureau'}, {'currency': '€', 'product': 'Lettre verte', 'price': 0.77, 'channel': 'en ligne'}, {'currency': '€', 'product': 'Lettre prioritaire', 'price': 0.95, 'channel': 'bureau'}, {'currency': '€', 'product': 'Lettre prioritaire', 'price': 0.92, 'channel': 'en ligne'}, {'currency': '€', 'product': 'Ecopli', 'price': 0.78, 'channel': 'bureau'}], status=200)

        r = self.api.tarifenvoi.get('lettre', 10)

        self.assertEqual(5, len(r))
        self.assertEqual('€', r[0].currency)
        self.assertEqual('Lettre verte', r[0].product)
        self.assertEqual(0.8, r[0].price)
        self.assertEqual('bureau', r[0].channel)

        self.assertEquals(len(responses.calls), 1)
        self.assertEquals(responses.calls[0].request.url, 'https://api.laposte.fr/tarifenvoi/v1/?type=lettre&poids=10')
        self.assertEquals(responses.calls[0].request.headers['X-Okapi-Key'], 'TheApiKey')

    @responses.activate
    def test_filters(self):
        responses.add(responses.GET,
                      'https://api.laposte.fr/tarifenvoi/v1/',
                      json=[{'currency': '€', 'product': 'Lettre verte', 'price': 0.8, 'channel': 'bureau'}, {'currency': '€', 'product': 'Lettre verte', 'price': 0.77, 'channel': 'en ligne'}, {'currency': '€', 'product': 'Lettre prioritaire', 'price': 0.95, 'channel': 'bureau'}, {'currency': '€', 'product': 'Lettre prioritaire', 'price': 0.92, 'channel': 'en ligne'}, {'currency': '€', 'product': 'Ecopli', 'price': 0.78, 'channel': 'bureau'}], status=200)

        r = self.api.tarifenvoi.get('lettre', 10, channels=[TarifEnvoiChannels.online], products=[TarifEnvoiProducts.first_class_mail])

        self.assertEqual(1, len(r))
        self.assertEqual('€', r[0].currency)
        self.assertEqual('Lettre prioritaire', r[0].product)
        self.assertEqual(0.92, r[0].price)
        self.assertEqual('en ligne', r[0].channel)

        self.assertEquals(len(responses.calls), 1)
        self.assertEquals(responses.calls[0].request.url, 'https://api.laposte.fr/tarifenvoi/v1/?type=lettre&poids=10')
        self.assertEquals(responses.calls[0].request.headers['X-Okapi-Key'], 'TheApiKey')


if __name__ == '__main__':
    unittest.main()
