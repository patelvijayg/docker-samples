#myclient = MongoClient("mongodb://mongodb2:mongodb2@localhost:27017/sampledb")
#myclient = MongoClient(host='localhost',port=27017,username='mongodb',password='mongodb',authSource='sampledb',authMechanism='SCRAM-SHA-1')
#myclient = MongoClient('ds121753.mlab.com',username='mongodb2',password='mongodb2',authSource='sampledb',authMechanism='SCRAM-SHA-256')

from pymongo import MongoClient
from models import testing
#mongouri='mongodb://localhost:27017'
mongouri='mongodb://mongodb2:mongodb2@ds121753.mlab.com:21753/sampledb'
myclient = MongoClient(mongouri)

def insert_one(empobject):
    with myclient:
        db = myclient.sampledb
        db.testing.insert_one(empobject.getJson()) 
        print("inserted ",empobject)

def find_one(id):
    with myclient:
        db = myclient.sampledb
        record=db.testing.find_one({"_id":id})
        print(record)
        return testing.from_json(record)

def delete_one(id):
    with myclient:
        db = myclient.sampledb
        db.testing.delete_one({"_id":id})
                
def convert_object():
    import json
    from collections import namedtuple
    data = '{"name": "John Smith", "hometown": {"name": "New York", "id": 123}}'
    # Parse JSON into an object with attributes corresponding to dict keys.
    x = json.loads(data, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
    return x

def test_insertone():
    with myclient:
        db = myclient.sampledb
        empobject=testing(1,'vijay',11.0,'2010-03-20')
        db.testing.insert_one(empobject.getJson()) 
        print("Run successfully")