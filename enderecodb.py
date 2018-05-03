from pymongo import MongoClient
import datetime

#comunicação com o servidor

client = MongoClient('192.168.1.14',28017, username='ivertex', password='123', authSource='admin', authMechanism='SCRAM-SHA-1')

#banco de dados

db = client.ivx_testebase

#coolection (tabela)

col = db.CADUSER

#variavel

endereco = {}

#Insert
col.insert_one(endereco)

#Find
#col.find_one({'numero': 102030})

#update
#col.update_one((num_guia), {'$set':{'numero':123}})

#delete
#col.delete_one(just)
