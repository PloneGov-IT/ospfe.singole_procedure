# -*- coding: utf-8 -*-

import re
from zope.interface import implements
from collective.tablepage.interfaces import IFieldValidator
from ospfe.singole_procedure import config
from ospfe.singole_procedure import _


class ValidatorCIG(object):
    """A string, max 10 chars"""
    implements(IFieldValidator)

    def __init__(self, field):
        self.field = field

    def validate(self, configuration):
        value = self.field.request.form.get(configuration['id'])
        if value and len(value)>10:
            return _('error_bad_cig', default='CIG must be a value of no more than 10 chars')


class ValidatorStrutturaProponente(object):
    """A string that match a proper format for struttura proponente (description and cf)"""
    implements(IFieldValidator)

    def __init__(self, field):
        self.field = field

    def validate(self, configuration):
        value = self.field.request.form.get(configuration['id'])
        match = re.match(config.STRUTTURA_PROPONENTE_MODEL, value, re.DOTALL)
        if value and not match:
            return _('error_bad_struttura_proponente',
                     default='You must provide a denomination, followed by a VAT or NIN')
        cf = match.groupdict()['cf']
        cf_match = re.match(config.CF_MODEL, cf, re.VERBOSE)
        if not cf_match:
            return _('error_bad_cf',
                     default='"$value" is not a valid VAT/NIN',
                     mapping={'value': cf})
