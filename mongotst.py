#myclient = MongoClient("mongodb://mongodb2:mongodb2@localhost:27017/sampledb")
#myclient = MongoClient(host='localhost',port=27017,username='mongodb',password='mongodb',authSource='sampledb',authMechanism='SCRAM-SHA-1')
#myclient = MongoClient('ds121753.mlab.com',username='mongodb2',password='mongodb2',authSource='sampledb',authMechanism='SCRAM-SHA-256')

from pymongo import MongoClient
myclient = MongoClient('mongodb://localhost:27017')
with myclient:
 db = myclient.sampledb
 c=testing(1,'vijay',11.0,'2010-03-20')
 db.testing.insert_one(c.getJson())   