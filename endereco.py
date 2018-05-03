
# coding: utf-8

# Endereço:


cep = str(input('Informe o número do CEP: '));
while (cep == 10):
    cep = str(input('Digite seu CEP novamente: '));

tipoendereco = str(input('Informe seu tipo de endereço: '));
while (tipoendereco == 10):
    tipoendereco = str(input('Digite seu tipo de endereço novamente: '));

endereco = str(input('Informe seu endereço completo: '));
while (endereco == 10):
    endereco = str(input('Digite seu endereço novamente: '));

complemento = str(input('Informe o complemento do seu endereço: '));
while (complemento == 10):
    complemento = str(input('informe o complemento do seu endereço novamente: '));

bairro = str(input('Informe o seu bairro: '));
while (bairro == 10):
    bairro = str(input('informe o seu bairro novamente: '));

estado = str(input('Informe o seu estado: '));
while (estado == 10):
    estado = str(input('informe o seu estado novamente: '));

cidade = str(input('Informe a sua cidade: '));
while (cidade == 10):
    cidade = str(input('informe a sua cidade novamente: '));

print ('\n\nDados: \n');
print ('\nCep:' + cep);
print ('\nTipoendereco:' + tipoendereco);
print ('\nEndereco:' + endereco);
print ('\nComplemento:' + complemento);
print ('\nBairro:' + bairro);
print ('\nEstado:' + estado);
print ('\nCidade:' + cidade);

