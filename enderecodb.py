from pymongo import MongoClient
import datetime

#comunicação com o servidor

client = MongoClient('192.168.1.14',28017, username='ivertex', password='123', authSource='admin', authMechanism='SCRAM-SHA-1')

#banco de dados

db = client.ivx_testebase

#coolection (tabela)

col = db.CADUSER

#variavel

endereco = {'CEP: ' : '71676-130', 'Tipo de Endereço: ' : 'Bairro', 'Endereço: ' : 'SHDB QL 32 Conjunto 6', 'Número: ' : '6', 'Complemento: ' : 'Villages Alvorada', 'Bairro' : 'Lago Sul' , 'Estado: ' : 'Distrito Federal', 'Cidade: ' : 'Brasília' , 'Data de Modificação: ' : datetime.datetime.utcnow()}

#Insert
col.insert_one(endereco)

#Find
#col.find_one({'numero': 102030})

#update
#col.update_one((num_guia), {'$set':{'numero':123}})

#delete
#col.delete_one(just)