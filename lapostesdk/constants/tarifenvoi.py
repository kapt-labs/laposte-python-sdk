# -*- coding:utf-8 -*-

# Standard library imports
from __future__ import unicode_literals

from enum import Enum


class TarifEnvoiTypes(Enum):
    letter = 'lettre'
    colissimo = 'colis'
    chronopost = 'chronopost'


class TarifEnvoiProducts(Enum):
    green_mail = 'Lettre verte'
    first_class_mail = 'Lettre prioritaire'
    ecopli = 'Ecopli'
    colissimo = 'Colissimo France (« avec Signature » en option)'
    chronopost_10 = 'Affranchissement Chronopost Chrono 10'
    chronopost_13 = 'Affranchissement Chronopost Chrono 13'


class TarifEnvoiChannels(Enum):
    post_office = 'bureau'
    online = 'en ligne'
