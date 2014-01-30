# -*- coding: utf-8 -*-

STRUTTURA_PROPONENTE_MODEL = r"""^\s*((?P<denominazione1>.+)\s+(?P<cf1>[a-zA-Z0-9]{11,}))|((?P<cf2>[a-zA-Z0-9]{11,})\s+(?P<denominazione2>.+))\s*$"""
CF_MODEL = r"""^(
    [A-Za-z]{6}[0-9]{2}[A-Za-z]{1}[0-9]{2}[A-Za-z]{1}[0-9A-Za-z]{3}[A-Za-z]{1} |
    [A-Za-z]{6}[0-9LMNPQRSTUV]{2}[A-Za-z]{1}[0-9LMNPQRSTUV]{2}[A-Za-z]{1}[0-9LMNPQRSTUV]{3}[A-Za-z]{1} |
    [0-9]{11,11}
)$"""
ACTORS_MODEL = r"""^\s*(((?P<ragione_sociale1>[^0-9].+)\s+(?P<cf1>[a-zA-Z0-9]{11,}))|((?P<cf2>[a-zA-Z0-9]{11,})\s+(?P<ragione_sociale2>[\(^0-9].+)))\s*$"""
GROUP_ACTORS_MODEL = r"""^\s*(((?P<ragione_sociale1>[^0-9].+)\s+(?P<cf1>[a-zA-Z0-9]{11,}))|((?P<cf2>[a-zA-Z0-9]{11,})\s+(?P<ragione_sociale2>[^0-9].+)))\s*\(\s*(?P<ruolo>[A-Z0-9-]+)\s*\)\s*$"""
DATES_MODEL = r"""^\s*(?P<start>\d\d\d\d-\d\d-\d\d)\s*[;\-/_ ]\s*(?P<end>\d\d\d\d-\d\d-\d\d)\s*$"""
IT_DATES_MODEL = r"""^\s*(?P<start_day>\d{1,2})[\-/](?P<start_month>\d{1,2})[\-/](?P<start_year>\d{4})\s*[;\-/_ ]\s*(?P<end_day>\d{1,2})[\-/](?P<end_month>\d{1,2})[\-/](?P<end_year>\d{4})\s*$""" 

SCELTA_CONTRAENTE_VOCABULARY = (
    "01-PROCEDURA APERTA",
    "02-PROCEDURA RISTRETTA",
    "03-PROCEDURA NEGOZIATA PREVIA PUBBLICAZIONE DEL BANDO",
    "04-PROCEDURA NEGOZIATA SENZA PREVIA PUBBLICAZIONE DEL BANDO",
    "05-DIALOGO COMPETITIVO",
    "06-PROCEDURA NEGOZIATA SENZA PREVIA INDIZIONE DI  GARA ART. 221 D.LGS. 163/2006",
    "07-SISTEMA DINAMICO DI ACQUISIZIONE",
    "08-AFFIDAMENTO IN ECONOMIA - COTTIMO FIDUCIARIO",
    "14-PROCEDURA SELETTIVA EX ART 238 C.7, D.LGS. 163/2006",
    "17-AFFIDAMENTO DIRETTO EX ART. 5 DELLA LEGGE N.381/91",
    "21-PROCEDURA RISTRETTA DERIVANTE DA AVVISI CON CUI SI INDICE LA GARA",
    "22-PROCEDURA NEGOZIATA DERIVANTE DA AVVISI CON CUI SI INDICE LA GARA",
    "23-AFFIDAMENTO IN ECONOMIA - AFFIDAMENTO DIRETTO",
    "24-AFFIDAMENTO DIRETTO A SOCIETA' IN HOUSE",
    "25-AFFIDAMENTO DIRETTO A SOCIETA' RAGGRUPPATE/CONSORZIATE O CONTROLLATE NELLE CONCESSIONI DI LL.PP",
    "26-AFFIDAMENTO DIRETTO IN ADESIONE AD ACCORDO QUADRO/CONVENZIONE",
    "27-CONFRONTO COMPETITIVO IN ADESIONE AD ACCORDO QUADRO/CONVENZIONE",
    "28-PROCEDURA AI SENSI DEI REGOLAMENTI DEGLI ORGANI COSTITUZIONALI",
)

RUOLO_VOCABULARY = (
    "01-MANDANTE",
    "02-MANDATARIA",
    "03-ASSOCIATA",
    "04-CAPOGRUPPO",
    "05-CONSORZIATA",
)