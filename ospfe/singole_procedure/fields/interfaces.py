# -*- coding: utf-8 -*-

from zope.interface import Interface
from collective.tablepage.interfaces import IColumnField
from collective.tablepage.fields.interfaces import ISelectColumnField

class ICIGColumnField(IColumnField):
    """A text field with CIG validator"""

class IStrutturaProponenteColumnField(IColumnField):
    """A text field with for struttura proponente"""

class IOggettoColumnField(IColumnField):
    """A text field for subject (limited to 250 chars)"""

class ISceltaContraenteColumnField(ISelectColumnField):
    """A select field with a well know vocabulary"""

class IOperatoriAggiudicatariColumnField(IColumnField):
    """A text area for storing data in a proper regex format for <partecipanti>/<aggiudicatari> nodes"""

class IMax250CharsColumnField(Interface):
    """Marker interface for column fields that must contains no more than 205 chars"""

class IDatesColumnField(Interface):
    """A text field for storing two dates"""
