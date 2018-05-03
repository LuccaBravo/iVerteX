
# coding: utf-8

# Pessoa:


nome = input('Nome: ');
while (len(nome) < 5 or len(nome) > 30):
    nome = input('Digite seu nome novamente: ');

sobrenome = input('Sobrenome: ');
while (len(sobrenome) < 5 or len(sobrenome) > 30):
    sobrenome = input('Digite seu sobrenome novamente: ');

sexo = input('Digite seu sexo: [F] or [M]: ');
while (sexo != 'M' and sexo != 'F'):
    sexo = input('Digite seu sexo novamente: [F] or [M]');

datadenascimento = str(input('Data de nascimento: '));
while (datadenascimento == 10):
    datadenascimento = str(input('Digite sua data de nascimento novamente: '));

cpf = str(input('CPF: '));
while (cpf == 14):
    cpf = str(input('Digite seu CPF novamente: '));

rg = str(input('RG: '));
while (rg == 9):
    rg = str(input('Digite seu RG novamente: '));

print ('\n\nDados: \n');
print ('\nNome:' + nome);
print ('\nSobrenome:' + sobrenome);
print ('\nSexo: ' + sexo);
print ('\nDatadenascimento: ' + datadenascimento);
print ('\nCpf: ' + cpf)
print ('\nRg: ' + rg)

