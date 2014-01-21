# -*- coding: utf-8 -*-

from collective.tablepage.fields.text import TextField
from collective.tablepage.fields.select import SelectField
from ospfe.singole_procedure import config
from ospfe.singole_procedure.fields.interfaces import ICIGColumnField
from ospfe.singole_procedure.fields.interfaces import IStrutturaProponenteColumnField
from ospfe.singole_procedure.fields.interfaces import ISceltaContraenteColumnField
from zope.interface import implements

try:
    from zope.browserpage.viewpagetemplatefile import ViewPageTemplateFile
except ImportError:
    # Plone < 4.1
    from zope.app.pagetemplate.viewpagetemplatefile import ViewPageTemplateFile


class CIGField(TextField):
    """A text field with CIG validator"""
    implements(ICIGColumnField)

    edit_template = ViewPageTemplateFile('cig.pt')


class StrutturaProponenteField(TextField):
    """A text field with for struttura proponente"""
    implements(IStrutturaProponenteColumnField)


class SceltaContraenteField(SelectField):
    implements(ISceltaContraenteColumnField)

    def vocabulary(self):
        # original vocabulary is ignored
        return list(config.SCELTA_CONTRAENTE_VOCABULARY)
