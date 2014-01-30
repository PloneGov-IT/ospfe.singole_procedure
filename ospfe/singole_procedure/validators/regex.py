# -*- coding: utf-8 -*-

import re
from zope.interface import implements
from collective.tablepage.interfaces import IFieldValidator
from ospfe.singole_procedure import config
from ospfe.singole_procedure import _


class ValidatorStrutturaProponente(object):
    """A string that match a proper format for struttura proponente (description and cf)"""
    implements(IFieldValidator)

    def __init__(self, field):
        self.field = field

    def validate(self, configuration, data=None):
        value = data or self.field.request.form.get(configuration['id'])
        match = re.match(config.STRUTTURA_PROPONENTE_MODEL, value, re.DOTALL)
        if value and not match:
            return _('error_bad_struttura_proponente',
                     default='You must provide a denomination, and a VAT or NIN')
        denominazione = match.groupdict().get('denominazione1') or match.groupdict().get('denominazione2')
        if len(denominazione)>250:
            return _('error_max_chars', default='The value for "$name" must contain no more than 250 characters ($count provided).',
                     mapping={'name': 'denominazione',
                              'count': len(denominazione)})

        cf = match.groupdict().get('cf1') or match.groupdict().get('cf2') 
        cf_match = re.match(config.CF_MODEL, cf, re.VERBOSE)
        if not cf_match:
            return _('error_bad_cf',
                     default='"$value" is not a valid VAT/NIN',
                     mapping={'value': cf})


class ValidatorOperatoriAggiudicatari(object):
    """Must fit a weel-defined regex"""
    implements(IFieldValidator)

    def __init__(self, field):
        self.field = field

    def validate(self, configuration, data=None):
        value = data or self.field.request.form.get(configuration['id'])
        value = value or ''
        lines = value.splitlines()
        results = []
        roles_count = 0
        groups_count = 1
        for i, l in enumerate(lines):
            l = l.strip()
            if not l:
                if roles_count==1:
                        return _('error_too_few_groups',
                                 default='Group $gcount. When groups are used, they must be composed by at least 2 members',
                                 mapping={'gcount': groups_count})            
                roles_count = 0
                groups_count += 1
                continue
            match1 = re.match(config.ACTORS_MODEL, l)
            match2 = re.match(config.GROUP_ACTORS_MODEL, l, re.VERBOSE)
            match = match2 or match1 or None
            if not match:
                return _('error_bad_member',
                         default='Line $line: not a proper format. Please insert a denomination followed by VAT/NIN.\n'
                                 'In case of a group, append also the role inside brackets',
                         mapping={'line': i+1})
            ragione_sociale = match.groupdict().get('ragione_sociale1') or match.groupdict().get('ragione_sociale2') or ''
            if len(ragione_sociale)>250:
                return _('error_max_chars',
                         default='A single denomination in the column "$name" must contain no more than 250 characters ($count provided).',
                         mapping={'name': configuration.get('label', configuration['id']).decode('utf-8'),
                                  'count': len(value)})

            cf = match.groupdict().get('cf1') or match.groupdict().get('cf2')
            cf_match = re.match(config.CF_MODEL, cf, re.VERBOSE)
            if not cf_match:
                return _('error_bad_member_cf',
                         default='Line $line: provided value \"$value\" for VAT/NIN is invalid.',
                         mapping={'line': i+1, 'value': cf})     
                       
            ruolo = match.groupdict().get('ruolo')
            if ruolo and ruolo not in config.RUOLO_VOCABULARY:
                return _('error_bad_roles',
                         default='Line $line: role \"$value\" is invalid. Must be one of the following: $roles',
                         mapping={'line': i+1, 'value': ruolo, 'roles': ', '.join(config.RUOLO_VOCABULARY)})
            elif ruolo:
                roles_count += 1


class ValidatorDates(object):
    """Two dates in the format YYYY-MM-DD, with a middle separator"""
    implements(IFieldValidator)

    def __init__(self, field):
        self.field = field

    def validate(self, configuration, data=None):
        value = data or self.field.request.form.get(configuration['id'])
        if value and not re.match(config.DATES_MODEL, value) and not re.match(config.IT_DATES_MODEL, value):
            return _('error_no_dates', default='Provide two dates in the format YYYY-MM-DD or DD-MM-YYYY')
