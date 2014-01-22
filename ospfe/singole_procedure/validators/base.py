# -*- coding: utf-8 -*-

from zope.interface import implements
from collective.tablepage.interfaces import IFieldValidator
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


class ValidatorMax250Chars(object):
    """A string, max 250 chars"""
    implements(IFieldValidator)

    def __init__(self, field):
        self.field = field

    def validate(self, configuration):
        col_id = configuration['id']
        value = self.field.request.form.get(configuration['id'])
        if value and len(value)>250:
            return _('error_max_chars', default='The value for "$name" must contain no more than 250 characters ($count provided).',
                     mapping={'name': configuration.get('label', col_id).decode('utf-8'),
                              'count': len(value)})

