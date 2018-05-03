from pymongo import MongoClient
import datetime

#comunicação com o servidor

client = MongoClient('192.168.1.14',28017, username='ivertex', password='123', authSource='admin', authMechanism='SCRAM-SHA-1')

#banco de dados

db = client.ivx_testebase

#coolection (tabela)

col = db.CADUSER

#variavel

pessoajuridica = {'CNPJ: ' : '37.136.082/0001-06', 'Razão Social: ' : 'REAL FREIOS, PECAS PARA VEICULOS, SERVICOS E TRANSPORTES LTDA - ME', 'Nome Fantasia: ' : 'REAL FREIOS PECAS E SERVICOS', 'IE: ' : 'N', 'IM: ' : 'N', 'Isento: ' : 'S', 'Data de Modificação: ' : datetime.datetime.utcnow()}

#Insert
col.insert_one(pessoajuridica)

#Find
#col.find_one({'numero': 102030})

#update
#col.update_one((num_guia), {'$set':{'numero':123}})

#delete
#col.delete_one(just)