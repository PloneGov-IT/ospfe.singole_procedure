# -*- coding: utf-8 -*-


from zope.interface import implements
from collective.tablepage.interfaces import IFieldValidator
from collective.tablepage import tablepageMessageFactory as tpmf
from ospfe.singole_procedure import config


class ValidatorEnforceVocabulary(object):
    """Validate that the data fit one of the vocabulary values (fixed vocabulary)"""
    implements(IFieldValidator)

    def __init__(self, field):
        self.field = field

    def validate(self, configuration):
        col_id = configuration['id']
        vocabulary = config.SCELTA_CONTRAENTE_VOCABULARY
        data = self.field.request.form.get(col_id)
        if data and data not in vocabulary:
            return tpmf('error_enforce_vocabulary',
                     default='The field "$name" does not fit any of the vocabulary values',
                     mapping={'name': configuration.get('label', col_id).decode('utf-8')})
