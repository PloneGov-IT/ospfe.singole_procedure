# -*- coding: utf-8 -*-

from collective.tablepage.interfaces import IColumnField
from collective.tablepage.fields.interfaces import ISelectColumnField


class ICIGColumnField(IColumnField):
    """A text field with CIG validator"""

class IStrutturaProponenteColumnField(IColumnField):
    """A text field with for struttura proponente"""

class ISceltaContraenteColumnField(ISelectColumnField):
    """A select field with a well know vocabulary"""
