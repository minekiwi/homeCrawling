from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import pprint
from dotenv import load_dotenv
import os 

##
#  데이터베이스 관리 기능을 제공하는 클래스
##

load_dotenv()

URL = os.getenv('dburi')
CLIENT = MongoClient(URL, server_api=ServerApi('1'))

def getCollection(databaseName, collectionName):
    db = CLIENT.get_database(databaseName)
    return db.get_collection(collectionName)

def update(collection, targetData, updateData, isUpsert):
    collection.update_one(targetData, updateData, upsert=isUpsert)

def delete(collection, targetData):
    collection.delete_one(targetData)