import pymongo
import os

class DbMongo:
    
    @staticmethod
    def getDB():
        user = ["USER"]
        password = ["PASSWORD"]
        cluster = ["CLUSTER"]
        query_string = "retryWrites=true&w=majority"
        
        
        mongo_uri = "mongodb://{0}:{1}@{2}/?{3}".format(
            user
            , password
            , cluster
            , query_string
        )            
        
        print(mongo_uri)
        
        client = pymongo.MongoClient(mongo_uri)
        db = client[os.environ["DB"]]
        
        return client, db