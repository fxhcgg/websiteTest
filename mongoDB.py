from pymongo import MongoClient
from config import Config
import platform
import certifi
import hashlib

if platform.system() == 'Windows':
    client = MongoClient(Config.MONGO_URI)
else:
    client = MongoClient(Config.MONGO_URI, tlsCAFile=certifi.where())
db = client['IndoorNavigation']

tester = db['tester']

def insert_tester(tester_name, password):
    hash_obj = hashlib.new(Config.ALGORITHM)
    hash_obj.update(password.encode('utf-8'))
    tester.insert_one({
        'tester_name': tester_name,
        'password': hash_obj.hexdigest(),
    })

def find_tester(tester_name,password):
    hash_obj = hashlib.new(Config.ALGORITHM)
    hash_obj.update(password.encode('utf-8'))
    return tester.find_one({
        'tester_name': tester_name, 
        'password': hash_obj.hexdigest()
    }) is not None
