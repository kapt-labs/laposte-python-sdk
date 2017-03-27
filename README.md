# La Poste SDK

![build status](https://travis-ci.org/geelweb/laposte-python-sdk.svg?branch=master)

LaPosteSDK is a Python client library to work with [La Poste API](https://developer.laposte.fr/products)

## Installation

    pip install lapostesdk

## Requirements

 - requests

Dev requirements

 - responses

## Configuration

    from lapostesdk.laposteapi import LaPosteApi
    api = LaPosteApi(api_key='YourApiKey')

## Test suite

    python -m unittest test

## Apis

### ControlAdresse

The [ControlAdresse Api](https://developer.laposte.fr/products/controladresse/latest)

**Address look up**

    response = api.controladresse.search('116 avenue du Président Kennedy 75220 Paris Cedex 16')

**Address details**

    adresse = api.controladresse.get('adresses/12280852')
    print adresse.codePostal

### Suivi

The [Suivi Api](https://developer.laposte.fr/products/suivi/latest)

    suivi = api.suivi.get('1111111111111')
    print suivi.status

