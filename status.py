
# coding: utf-8

# Status:


tipostatus = input('Digite o Status do convênio/plano: [ATIVO] or [INATIVO]: ');
while (tipostatus != 'ATIVO' and tipostatus != 'INATIVO'):
    tipostatus = input('Digite o Status do convênio/plano novamente: [ATIVO] or [INATIVO]');

import datetime

print ('\n\nDados: \n');
print ('\nTipostatus:' + tipostatus);
print datetime.datetime.utcnow()
