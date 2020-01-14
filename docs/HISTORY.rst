Changelog
=========

0.3.4 (2020-01-14)
------------------

- Changed check on effective date. Updated schema as requested.
  [daniele]


0.3.3 (2019-12-11)
------------------

- Updated TypesL190.xsd
  [daniele]

0.3.2 (2019-29-01)
------------------

- Updated TypesL190.xsd
  [daniele]

0.3.1 (2015-01-30)
------------------

- Migliorata affidabilità regexp
  [keul]

0.3.0 (2015-01-15)
------------------

Verifiche di compatibilità con Plone 4.3

- ``annoRiferimento`` viene letto (potenzialmente) da una CMF property.
  Il default rimane al 2013 per compatibilità con l'anno scorso
  [keul]
- Aggiunge funzionalità di debug
  [keul]
- Fix alle regex per gestire casi sfortunati in cui la denominazione può essere
  scambiata per un C.F. o P. IVA.
  [keul]
- Importi nella vista di generazione XML ora sempre in formato stringa
  [keul]
- Rinominata colonna "*Date*" in "*Dal-Al*" per namespace clash con
  nuove colonne di tablepage 0.10
  [keul]

0.2.0 (2014-01-31)
------------------

- Bug: la presenza di costi con valore ``0.00`` non mostrava il nodo
  [keul]
- Permessa la presenza di codice fiscale/P.I. prima della ragione sociale
  (con qualche limite)
  [keul]

0.1.0 (2014-01-29)
------------------

- Initial release
