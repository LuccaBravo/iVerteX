from pymongo import MongoClient
import datetime

#comunicação com o servidor

client = MongoClient('192.168.1.14',28017, username='ivertex', password='123', authSource='admin', authMechanism='SCRAM-SHA-1')

#banco de dados

db = client.ivx_testebase

#coolection (tabela)

col = db.CADUSER

#variavel

contato = {'Telefone: ' : '061-98277-7007', 'E-Mail: ' : 'bizinoto.jus@gmail.com', 'WebSite: ' : 'www.ivertex.com.br' , 'Data de Modificação: ' : datetime.datetime.utcnow()}

#Insert
col.insert_one(contato)

#Find
#col.find_one({'numero': 102030})

#update
#col.update_one((num_guia), {'$set':{'numero':123}})

#delete
#col.delete_one(just)