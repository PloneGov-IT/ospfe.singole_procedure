# -*- coding: utf-8 -*-

from collective.tablepage.fields.text import TextField
from collective.tablepage.fields.text import TextAreaField
from collective.tablepage.fields.select import SelectField
from ospfe.singole_procedure import config
from ospfe.singole_procedure.fields.interfaces import ICIGColumnField
from ospfe.singole_procedure.fields.interfaces import IStrutturaProponenteColumnField
from ospfe.singole_procedure.fields.interfaces import IOggettoColumnField
from ospfe.singole_procedure.fields.interfaces import ISceltaContraenteColumnField
from ospfe.singole_procedure.fields.interfaces import IOperatoriAggiudicatariColumnField
from ospfe.singole_procedure.fields.interfaces import IDatesColumnField
from ospfe.singole_procedure.fields.interfaces import IMax250CharsColumnField
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
    """A text field for struttura proponente"""
    implements(IStrutturaProponenteColumnField)


class OggettoField(TextAreaField):
    """A text field for subject (limited to 250 chars)"""
    implements(IOggettoColumnField, IMax250CharsColumnField)

    def __init__(self, context, request):
        TextAreaField.__init__(self, context, request)
        self.rows = 10


class OperatoriAggiudicatariField(TextAreaField):
    """A text area for storing data in a proper regex format for <partecipanti>/<aggiudicatari> nodes"""
    implements(IOperatoriAggiudicatariColumnField)

    def __init__(self, context, request):
        TextAreaField.__init__(self, context, request)
        self.rows = 10


class SceltaContraenteField(SelectField):
    implements(ISceltaContraenteColumnField)

    def vocabulary(self):
        # original vocabulary is ignored
        return list(config.SCELTA_CONTRAENTE_VOCABULARY)


class DatesField(TextField):
    """A text field for storing two dates"""
    implements(IDatesColumnField)
