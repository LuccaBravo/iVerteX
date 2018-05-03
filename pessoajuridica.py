
# coding: utf-8

# Pessoa Jurídica:


cnpj = str(input('Informe o CNPJ da sua empresa: '));
while (cnpjc == 10):
    cnpj = str(input('Informe o CNPJ da sua empresa novamente: '));

razaosocial = str(input('Informe o número da Razão Social: '));
while (razaosocial == 10):
    razaosocial = str(input('Informe o número da Razão Social novamente: '));

fantasia = str(input('Informe o nome fantasia da sua empresa: '));
while (fantasia == 10):
    fantasia = str(input('Informe o nome fantasia da sua empresa novamente: '));

im = str(input('Informe sua Inscrição Municipal: '));
while (im == 10):
    im = str(input('Informe sua Inscrição Municipal novamente: '));

ie = str(input('Informe sua Inscrição Estadual: '));
while (ie == 10):
    ie = str(input('Informe sua Inscrição Estadual novamente: '));

isento = input('Informe se é Isento, digite SIM ou NAO: [SIM] or [NAO]: ');
while (isento != 'SIM' and isento != 'NAO'):
    isento = input('Informe se é Isento, digite SIM ou NAO: [SIM] or [NAO] novamente: [SIM] or [NAO]');

print ('\n\nDados: \n');
print ('\nCnpj:' + cnpj);
print ('\nRazaosocial:' + razaosocial);
print ('\nFantasia: ' + fantasia);
print ('\nIm: ' + im);
print ('\nIe: ' + ie);
print ('\nIsento: ' + isento);

