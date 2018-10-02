# -*- coding:utf-8 -*-

# Standard library imports
from __future__ import unicode_literals

from lapostesdk.entities.base import BaseEntity


class Adresse(BaseEntity):
    def __init__(self):
        self.destinataire = None
        self.pointRemise = None
        self.numeroVoie = None
        self.libelleVoie = None
        self.lieuDit = None
        self.codePostal = None
        self.codeCedex = None
        self.commune = None
        self.blocAdresse = None
