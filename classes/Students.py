from classes.DbMongo import DbMongo


class Students:
       
    def __init__(self, fullname, account_number, age):
        self.fullname = fullname
        self.account_number = account_number
        self.age = age
        self.__collection = "students"
        
    def save(self, db):
        collection = db[self.__collection]
        collection.insert_one(self.__dict__)
    
        
          