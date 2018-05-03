
# coding: utf-8

# Contato:


telefone = int(input('Digite seu telefone: '));
while (telefone == 10):
    telefone = int(input('Digite seu telefone novamente: '));

email = str(input('Digite seu Email: '));
while (email == 10):
    email = str(input('Digite seu Email novamente: '));

site = str(input('Digite seu Site: '));
while (site == 10):
    site = str(input('Digite seu Site novamente: '));


print ('\n\nDados: \n');
print ('\nTelefone:' + telefone);
print ('\nEmail:' + email);
print ('\nSite: ' + site);