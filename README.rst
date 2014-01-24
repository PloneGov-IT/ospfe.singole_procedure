Questo prodotto si occupa di aggiungere alcune funzionalità a `collective.tablepage`__ per gestire i casi in cui
il prodotto sia stato usato per sopperire alle richieste dell'`art. 1 comma 32 Legge n. 190/2012`__ e che sia quindi
necessario esporre i dati in formato XML.

__ http://plone.org/products/collective.tablepage
__ http://www.avcp.it/portal/public/classic/AttivitaAutorita/AttiDellAutorita/_Atto?ca=5397

.. image:: http://blog.redturtle.it/pypi-images/ospfe.singole_procedure/ospfe.singole_procedure-0.1.0-02.png/image_large
   :alt: Configurazione tabella
   :target: http://blog.redturtle.it/pypi-images/ospfe.singole_procedure/ospfe.singole_procedure-0.1.0-02.png
   :align: center

.. contents::

Installazione
=============

Il prodotto non è rilasciato ufficialmente sul `Cheeseshop`__, per poterlo installare da buildout è necessario
modificare la configurazione del medesimo::

    [buildout]
    ...
    find-links =
        ...
        https://github.com/PloneGov-IT/ospfe.singole_procedure/releases/download/x.y.z/ospfe.singole_procedure-x.y.z.zip

... dove *x.y.z* rappresenta la versione del prodotto da utilizzare, ad esempio::

    https://github.com/PloneGov-IT/ospfe.singole_procedure/releases/download/0.1.0/ospfe.singole_procedure-0.1.0.zip

__ http://pypi.python.org/

Come usarlo
===========

Attivazione
-----------

Va scelta una pagina con tabella specifica e va aggiunta un'interfaccia marcatore. Per fare questo va richiamato
l'URL del documento aggiungendovi in fondo "/manage_interfaces". Esempio:

    http://host.com/percorso/alla/pagina-con-tabella/manage_interfaces

L'interfaccia da aggiungere è ``ospfe.singole_procedure.interfaces.ISingoleProcedureInterface``.

Da questo momento in poi questa singola pagina con tabella ha nuove funzionalità sotto descritte.

Nuove colonne
-------------

Il prodotto aggiunge una serie di nuovi tipi di colonne al solo scopo di aiutrare la compilazione della tabella.

``CIG``
    Un campo stringa di non più di 10 caratteri
``Struttura proponente``
    Un campo stringa che al salvataggio verifica i dati inseriti.
    
    Tali dati *devono* includere una denominazione (massimo 250 caratteri) seguita o receduta dal codice fiscale o partita I.V.A.
``Oggetto``
    Oggetto del bando, limitato a 250 caratteri
``Procedura scelta contraente``
    Un campo di selezione che già utilizza il vocabolario definito dallo schema XSD, senza doverlo configurare.
``Operatori / Aggiudicatari``
    Un campo valido per entrambi i tipi di dato. Permette di definire una sequenza (un elemento per riga) di partecipanti
    o aggiundicatari del bando.
        
    Ogni elemento deve essere composto dalla denominazione seguita dal codice fiscale o partita I.V.A.
    
    In presenza di consorziate va infine posto (tra parentesi) il ruolo, secondo il vocabolario definito dallo schema XSD.
    Le corsorziate definiscono quindi un gruppo, che va separato dagli altri gruppi, o dai partecipanti/aggiudicatari singoli,
    da una riga vuota.
``Date``
    Un campo stringa per l'inserimento delle due date. Le date devono essere nel formato AAAA-MM-GG o anche nel
    formato GG-MM-AAAA, e possono essere separate da un carattere separatore quale "-", "/".

Dato che non si vuole "inquinare" il normale uso della pagina con tabella, l'attivazione delle nuove colonne avviene
in modo puntuale.

Struttura del documento
-----------------------

.. image:: http://blog.redturtle.it/pypi-images/ospfe.singole_procedure/ospfe.singole_procedure-0.1.0-01.png/image_preview
   :alt: Configurazione tabella
   :target: http://blog.redturtle.it/pypi-images/ospfe.singole_procedure/ospfe.singole_procedure-0.1.0-01.png
   :align: right

Il prodotto da' per scontato che la tabella generata abbia una ben definita struttura a *9 colonne* e che gli
id delle colonne siano:

* cig (consigliato uso della colonna "CIG" e obbligatorietà)
* struttura_proponente (consigliato uso della colonna "Struttura proponente" e obbligatorietà)
* oggetto_bando (consigliato uso della colonna "Oggetto" e obbligatorietà)
* procedura_scelta (consigliato uso della colonna "Procedura scelta contraente")
* elenco_operatori (consigliato uso della colonna "Operatori / Aggiudicatari")
* aggiudicatario (consigliato uso della colonna "Operatori / Aggiudicatari")
* importo_aggiudicazione (consigliato uso della colonna "Numerico" o "Monetario")
* tempi_completamento (consigliato uso della colonna "Date")
* importo_somme_liquidate (consigliato uso della colonna "Numerico" o "Monetario")

XML e Validazione
=================

Il file XML richiesto dalla normativa è sempre disponibile richiamando la vista **dataset.xml** sulla pagina con tabella.
Per esempio:

    http://host.com/percorso/alla/pagina-con-tabella/dataset.xml

Prima di esporre il sorgente XML è possibile effettuare una validazione dello stesso. Dalla pagina di modifica della tabella
sarà ora disponibile un nuovo link "*Valida XML*", che eseguirà la validazione secondo lo schema fornito da AVCP.

.. image:: http://blog.redturtle.it/pypi-images/ospfe.singole_procedure/ospfe.singole_procedure-0.1.0-03.png/image_large
   :alt: Configurazione tabella
   :target: http://blog.redturtle.it/pypi-images/ospfe.singole_procedure/ospfe.singole_procedure-0.1.0-03.png
   :align: center

Dipendenze e versioni
=====================

Il prodotto è stato testato su Plone 3.3, ma *dovrebbe* funzionare senza problemi anche su Plone 4.

Limiti
======

Non viene fornito un XML per l'indice dei dataset. Ipoteticamente potrebbe essere fatto con una vista apposita
sugli oggetti Collezione.

Crediti
=======

Sviluppato col supporto dell'`Ospedale S. Anna, Ferrara`__; l'Ospedale S. Anna supporta
`l'iniziativa PloneGov`__.

.. image:: http://www.ospfe.it/ospfe-logo.jpg
   :alt: OspFE logo

__ http://www.ospfe.it/
__ http://www.plonegov.it/

Autori
=======

Questo prodotto è stato sviluppato da RedTurtle Technology.

.. image:: http://www.redturtle.it/redturtle_banner.png
   :alt: RedTurtle Technology Site
   :target: http://www.redturtle.it/
