#!/bin/sh

DOMAIN='ospfe.singole_procedure'

i18ndude rebuild-pot --pot ./${DOMAIN}.pot --merge ./${DOMAIN}-manual.pot --create ${DOMAIN} ..
i18ndude sync --pot ./${DOMAIN}.pot ./*/LC_MESSAGES/${DOMAIN}.po
