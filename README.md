# La Poste SDK

LaPosteSDK is a Python client library to work with [La Poste API](https://developer.laposte.fr/products)

## Installation

    pip install lapostesdk

## Requirements

 - requests

## Configuration

    from lapostesdk.laposteapi import LaPosteApi
    api = LaPosteApi(api_key='YourApiKey')

## Apis

### ControlAdresse

The [ControlAdresse Api](https://developer.laposte.fr/products/controladresse/latest)

**Address look up**

    api.controladresse.search('116 avenue du Président Kennedy 75220 Paris Cedex 16')

**Address details**

    api.controladresse.get('adresses/12280852')


### Suivi

The [Suivi Api](https://developer.laposte.fr/products/suivi/latest)

    api.suivi.get('1111111111111')

