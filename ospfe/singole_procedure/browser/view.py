# -*- coding: utf-8 -*-

import re
import lxml

from Products.CMFCore.utils import getToolByName
from Products.Five.browser import BrowserView
from StringIO import StringIO
from collective.tablepage.interfaces import IDataStorage
from ospfe.singole_procedure import config


class SingoleProcedureXMLView(BrowserView):
    """Rendere XML as defined by http://dati.avcp.it/schema/datasetAppaltiL190.xsd"""

    def __call__(self, *args, **kwargs):
        self.request.response.setHeader('Content-Type', 'text/xml')
        return self.index()

    def effective(self):
        if self.context.getEffectiveDate():
            return self.context.getEffectiveDate().strftime('%Y-%m-%d')
        return self.context.created().strftime('%Y-%m-%d')

    def modified(self):
        return self.context.modified().strftime('%Y-%m-%d')

    def rows(self):
        """Iterate on rows on the table"""
        rows = []
        for item in IDataStorage(self.context):
            try:
                importo_aggiudicazione = float(item.get('importo_aggiudicazione') or '')
            except ValueError:
                importo_aggiudicazione = None
            try:
                importo_somme_liquidate = float(item.get('importo_somme_liquidate') or '')
            except ValueError:
                importo_somme_liquidate = None
            
            row = {
                   'cig': item.get('cig'),
                   'struttura_proponente': self._get_struttura_proponente(item.get('struttura_proponente', '')),
                   'oggetto_bando': item.get('oggetto_bando', ''),
                   'procedura_scelta': (item.get('procedura_scelta', '') in config.SCELTA_CONTRAENTE_VOCABULARY and item.get('procedura_scelta', '') or ''),
                   'elenco_operatori': self._get_actors(item.get('elenco_operatori', '')),
                   'aggiudicatario': self._get_actors(item.get('aggiudicatario', '')),
                   'importo_aggiudicazione': importo_aggiudicazione,
                   'tempi_completamento': self._get_tempi_completamento(item.get('tempi_completamento', '')),
                   'importo_somme_liquidate': importo_somme_liquidate,
                   }
            rows.append(row)
        return rows

    def _get_struttura_proponente(self, data):
        """Return a dict as with 'cf' and 'denominazione' items"""
        result = {'cf': '', 'denominazione': ''}
        match = re.match(config.STRUTTURA_PROPONENTE_MODEL, data, re.DOTALL)
        if match:
            cf = match.groupdict()['cf']
            result['denominazione'] = match.groupdict()['denominazione']
            cf_match = re.match(config.CF_MODEL, cf, re.VERBOSE)
            if cf_match:
                result['cf'] = cf
        return result

    def _get_actors(self, data):
        """Return a list of dicts with two possible formats:
            ragione_sociale, cf ruolo
        or
            ragione_sociale, cf
        """
        # This fix some strange nully data from the storage get
        data = data or ''
        lines = data.splitlines()
        results = []
        for l in lines:
            result = {'cf': '', 'ragione_sociale': '', 'ruolo': ''}
            match = re.match(config.ACTORS_MODEL, l)
            if match:
                cf = match.groupdict()['cf']
                result['ragione_sociale'] = match.groupdict()['ragione_sociale']
                ruolo = match.groupdict()['ruolo']
                cf_match = re.match(config.CF_MODEL, cf, re.VERBOSE)
                if cf_match:
                    result['cf'] = cf
                result['ruolo'] = ruolo in config.RUOLO_VOCABULARY and ruolo or ''
                results.append(result)
        return results

    def _get_tempi_completamento(self, data):
        """Get two dates from the data"""
        data = data or ''
        result = {'dstart': '', 'dend': ''}
        match = re.match(config.DATES_MODEL, data)
        if match:
            result['dstart'] = match.groupdict()['start']
            result['dend'] = match.groupdict()['end']
        return result


class XMLValidationView(BrowserView):
    """A view that show validation report"""

    def __init__(self, context, request):
        self.context = context
        self.request = request
        request.set('disable_border', True)
        self.errors = None

    def validate(self):
        context = self.context
        xml_source = StringIO(context.restrictedTraverse('@@dataset.xml')().encode('utf-8'))
        portal = getToolByName(context, 'portal_url').getPortalObject()
        xsd_source = portal.restrictedTraverse('++resource++ospfe.singole_procedure.resources/datasetAppaltiL190.xsd')
        f = open(xsd_source.context.path)
        xmlschema_doc = lxml.etree.parse(f)
        f.close()
        xmlschema = lxml.etree.XMLSchema(xmlschema_doc)
        try:
            xmlschema.assertValid(lxml.etree.parse(xml_source))
        except lxml.etree.DocumentInvalid, inst:
            self.errors = str(inst)

    def __call__(self):
        self.validate()
        return self.index()

