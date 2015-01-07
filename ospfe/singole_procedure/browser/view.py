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

    def __init__(self, context, request):
        BrowserView.__init__(self, context, request)
        self.strip_invalid = True

    def __call__(self, *args, **kwargs):
        self.request.response.setHeader('Content-Type', 'text/xml')
        return self.index()

    def effective(self):
        if self.context.getEffectiveDate():
            return self.context.getEffectiveDate().strftime('%Y-%m-%d')
        return self.context.created().strftime('%Y-%m-%d')

    def modified(self):
        return self.context.modified().strftime('%Y-%m-%d')

    def anno_riferimento(self):
        return self.context.getProperty('anno_riferimento', None) or '2013'

    def rows(self, storage=None, headers=None):
        """Iterate on rows on the table"""
        rows = []
        storage = storage or IDataStorage(self.context)
        for item in storage:

            if not headers:
                configuration = self.context.getPageColumns()
                headers = [h['id'] for h in configuration]
            
            try:
                importo_aggiudicazione = "%0.2f" % float(item.get(headers[6]) or '')
            except ValueError:
                importo_aggiudicazione = "0.00"
            try:
                importo_somme_liquidate = "%0.2f" % float(item.get(headers[8]) or '')
            except ValueError:
                importo_somme_liquidate = "0.00"
            row = {
                   'cig': item.get(headers[0]) or '0000000000',
                   'struttura_proponente': self._get_struttura_proponente(item.get(headers[1], '')),
                   'oggetto_bando': item.get(headers[2], ''),
                   'procedura_scelta': item.get(headers[3], ''),
                   'partecipantiRaggruppamento': self._get_groups_actors(item.get(headers[4], '')),
                   'partecipanti': self._get_actors(item.get(headers[4], '')),
                   'aggiudicatarioRaggruppamento': self._get_groups_actors(item.get(headers[5], '')),
                   'aggiudicatario': self._get_actors(item.get(headers[5], '')),
                   'importo_aggiudicazione': importo_aggiudicazione,
                   'tempi_completamento': self._get_tempi_completamento(item.get(headers[7], '')),
                   'importo_somme_liquidate': importo_somme_liquidate,
                   }
            rows.append(row)
        return rows

    def _get_struttura_proponente(self, data):
        """Return a dict as with 'cf' and 'denominazione' items"""
        result = {'cf': '', 'denominazione': ''}
        match = re.match(config.STRUTTURA_PROPONENTE_MODEL, data, re.DOTALL)
        if match:
            cf = match.groupdict().get('cf1') or match.groupdict().get('cf2') 
            result['denominazione'] = match.groupdict().get('denominazione1') or match.groupdict().get('denominazione2')
            cf_match = re.match(config.CF_MODEL, cf, re.VERBOSE)
            if cf_match or not self.strip_invalid:
                result['cf'] = cf
        elif not self.strip_invalid:
            return {'cf': data, 'denominazione': data}
        return result

    def _get_groups_actors(self, data):
        """Return a list of list of dicts composed as ragione_sociale, cf, ruolo"""
        # This fix some strange nully data from the storage get
        data = data or ''
        results = []
        data = data.replace("\r", '')
        groups = data.split("\n\n")
        for g in groups:
            inner_result = []
            for l in g.splitlines():
                match = re.match(config.GROUP_ACTORS_MODEL, l, re.VERBOSE)
                if match:
                    result = {'cf': '', 'ragione_sociale': '', 'ruolo': ''}
                    result['ragione_sociale'] = match.groupdict().get('ragione_sociale1') or match.groupdict().get('ragione_sociale2')
                    cf = match.groupdict().get('cf1') or match.groupdict().get('cf2')
                    cf_match = re.match(config.CF_MODEL, cf, re.VERBOSE)
                    if cf_match or not self.strip_invalid:
                        result['cf'] = cf
                    result['ruolo'] = match.groupdict()['ruolo']
                    inner_result.append(result)
                elif not self.strip_invalid:
                    inner_result.append({'cf': l, 'ragione_sociale': l, 'ruolo': l})
            if inner_result:
                results.append(inner_result)
        return results

    def _get_actors(self, data):
        """Return a list dicts composed as ragione_sociale, cf"""
        # This fix some strange nully data from the storage get
        data = data or ''
        lines = data.splitlines()
        results = []
        for l in lines:
            match = re.match(config.ACTORS_MODEL, l)
            if match:
                result = {'cf': '', 'ragione_sociale': '', }
                result['ragione_sociale'] = match.groupdict().get('ragione_sociale1') or match.groupdict().get('ragione_sociale2')
                cf = match.groupdict().get('cf1') or match.groupdict().get('cf2')
                cf_match = re.match(config.CF_MODEL, cf, re.VERBOSE)
                if cf_match or not self.strip_invalid:
                    result['cf'] = cf
                results.append(result)
            elif not self.strip_invalid:
                results.append({'cf': l, 'ragione_sociale': l, })
        return results

    def _get_tempi_completamento(self, data):
        """Get two dates from the data"""
        data = data or ''
        result = {'dstart': '', 'dend': ''}
        # 1. already in the good format
        match = re.match(config.DATES_MODEL, data)
        if match:
            result['dstart'] = match.groupdict()['start']
            result['dend'] = match.groupdict()['end']
        elif not self.strip_invalid:
            result['dstart'] = result['dend'] = data
        else:
            # 2. in the italian format
            match = re.match(config.IT_DATES_MODEL, data)
            if match:
                year = match.groupdict()['start_year']
                month = match.groupdict()['start_month']
                month = len(month)<2 and "0%s" % month or month
                day = match.groupdict()['start_day']
                day = len(day)<2 and "0%s" % day or day
                result['dstart'] = "%s-%s-%s" % (year, month, day)

                year = match.groupdict()['end_year']
                month = match.groupdict()['end_month']
                month = len(month)<2 and "0%s" % month or month
                day = match.groupdict()['end_day']
                day = len(day)<2 and "0%s" % day or day
                result['dend'] = "%s-%s-%s" % (year, month, day)
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
            self.errors = inst.args[0].encode('utf-8')

    def __call__(self):
        self.validate()
        return self.index()
