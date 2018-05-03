from pymongo import MongoClient
import datetime

#comunicação com o servidor

client = MongoClient('192.168.1.14',28017, username='ivertex', password='123', authSource='admin', authMechanism='SCRAM-SHA-1')

#banco de dados

db = client.ivx_testebase

#coolection (tabela)

col = db.CADUSER

#variavel

pessoa = {'Nome: ' : 'Lucas Ciryllo', 'Sobrenome: ' : 'Moreira Bizinoto', 'Sexo: ' : 'M', 'Data de Nascimento: ' : '08/10/1991' , 'CPF: ' : '04437851129', 'RG: ' : '2508448', 'Data de Modificação: ' : datetime.datetime.utcnow()}

#Insert
col.insert_one(pessoa)

#Find
#col.find_one({'numero': 102030})

#update
#col.update_one((num_guia), {'$set':{'numero':123}})

#delete
#col.delete_one(just)