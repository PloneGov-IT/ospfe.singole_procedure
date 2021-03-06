Questo prodotto si occupa di aggiungere alcune funzionalità a `collective.tablepage`__ per gestire i casi in cui
il prodotto sia stato usato per sopperire alle richieste dell'`art. 1 comma 32 Legge n. 190/2012`__ e che sia quindi
necessario esporre i dati in formato XML.

__ http://plone.org/products/collective.tablepage
__ http://www.avcp.it/portal/public/classic/AttivitaAutorita/AttiDellAutorita/_Atto?ca=5397

.. image:: http://blog.redturtle.it/pypi-images/ospfe.singole_procedure/ospfe.singole_procedure-0.1.0-02.png/image_large
   :alt: Configurazione tabella
   :target: http://blog.redturtle.it/pypi-images/ospfe.singole_procedure/ospfe.singole_procedure-0.1.0-02.png
   :align: center

Una copia delle specifiche tecniche è inclusa nel sorgente del prodotto.

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

    https://github.com/PloneGov-IT/ospfe.singole_procedure/releases/download/0.3.0/ospfe.singole_procedure-0.3.0.zip

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
    
    Tali dati *devono* includere una denominazione (massimo 250 caratteri) seguita o preceduta dal codice fiscale o
    partita I.V.A.
``Oggetto``
    Oggetto del bando, limitato a 250 caratteri
``Procedura scelta contraente``
    Un campo di selezione che già utilizza il vocabolario definito dallo schema XSD, senza doverlo configurare.
``Operatori / Aggiudicatari``
    Un campo valido per entrambi i tipi di dato. Permette di definire una sequenza (un elemento per riga) di partecipanti
    o aggiundicatari del bando.
        
    Ogni elemento deve essere composto dalla denominazione seguita dal codice fiscale o partita I.V.A.
    
    In presenza di consorziate va infine posto (tra parentesi) il ruolo, secondo il vocabolario definito dallo schema XSD.
    Le corsorziate definiscono quindi un gruppo, che va separato dagli altri gruppi, o dai partecipanti/aggiudicatari
    singoli,
    da una riga vuota.
``Dal-Al``
    Un campo stringa per l'inserimento delle due date. Le date devono essere nel formato AAAA-MM-GG o anche nel
    formato GG-MM-AAAA, e possono essere separate da un carattere separatore quale "-" e "/".

Dato che non si vuole "inquinare" il normale uso della pagina con tabella, l'attivazione delle nuove colonne avviene
in modo puntuale previa attivazione dell'interfaccia, come discusso alla sezione precedente.

Struttura del documento
-----------------------

.. image:: http://blog.redturtle.it/pypi-images/ospfe.singole_procedure/ospfe.singole_procedure-0.1.0-01.png/image_preview
   :alt: Configurazione tabella
   :target: http://blog.redturtle.it/pypi-images/ospfe.singole_procedure/ospfe.singole_procedure-0.1.0-01.png
   :align: right

Il prodotto da' per scontato che la tabella generata abbia una ben definita struttura a *9 colonne*
definite in questo ordine:

* **CIG** - consigliato uso della colonna "CIG" (non obbligatorio, vedere `le FAQ`__)
* **Struttura proponente**  - consigliato uso della colonna "Struttura proponente" e obbligatorietà
* **Oggetto del bando** - consigliato uso della colonna "Oggetto" e obbligatorietà
* **Procedura di scelta del contraente** - consigliato uso della colonna "Procedura scelta contraente"
* **Elenco operatori** - consigliato uso della colonna "Operatori / Aggiudicatari"
* **Aggiudicatario** - consigliato uso della colonna "Operatori / Aggiudicatari"
* **Importo di aggiudicazione** - consigliato uso della colonna "Numerico" o "Monetario"
* **Tempi completamento** - consigliato uso della colonna "Dal-Al"
* **Importo somme liquidate** - consigliato uso della colonna "Numerico" o "Monetario"

__ http://www.avcp.it/portal/public/classic/FAQ/faq_legge190_2012#sezioneC

XML e Validazione
=================

Il file XML richiesto dalla normativa è sempre disponibile richiamando la vista **dataset.xml** sulla pagina con tabella.
Per esempio:

    http://host.com/percorso/alla/pagina-con-tabella/dataset.xml

Prima di esporre il sorgente XML è possibile effettuare una validazione dello stesso. Dalla pagina di modifica della
tabella sarà ora disponibile un nuovo link "*Valida XML*", che eseguirà la validazione secondo lo schema fornito da AVCP.

.. image:: http://blog.redturtle.it/pypi-images/ospfe.singole_procedure/ospfe.singole_procedure-0.1.0-03.png/image_large
   :alt: Configurazione tabella
   :target: http://blog.redturtle.it/pypi-images/ospfe.singole_procedure/ospfe.singole_procedure-0.1.0-03.png
   :align: center

Dato ``annoRiferimento``
------------------------

All'interno del file XML generato è presente un elemento ``annoRiferimento`` che di base viene valorizzato a
*2013*. È possibile cambiare tale scelta aggiungendo al contenuto una CMF property di nome ``anno_riferimento``.

Dipendenze e versioni
=====================

Il prodotto è stato testato su Plone 4.3, ma *dovrebbe* ancora funzionare senza problemi anche su Plone 3.3.

Limiti
======

Non viene fornito un XML per l'indice dei dataset. Ipoteticamente potrebbe essere fatto con una vista apposita
sugli oggetti Collezione (`pull request`__ a riguardo sono ben accette!).

__ https://github.com/PloneGov-IT/ospfe.singole_procedure/pulls

Crediti
=======

Sviluppato col supporto di:

* `Ospedale Sant'Anna, Ferrara`__

  .. image:: http://www.ospfe.it/ospfe-logo.jpg 
     :alt: Logo Ospedale S. Anna
  
* `Azienda USL Ferrara`__

  .. image:: http://www.ausl.fe.it/logo_ausl.gif
     :alt: Logo Azienda AUSL

Questi enti supportano `L'iniziativa PloneGov`__.

__ http://www.ospfe.it/
__ http://www.ausl.fe.it/
__ http://www.plonegov.it/

Autori
======

Questo prodotto è stato sviluppato da RedTurtle Technology.

.. image:: http://www.redturtle.it/redturtle_banner.png
   :alt: RedTurtle Technology Site
   :target: http://www.redturtle.it/
