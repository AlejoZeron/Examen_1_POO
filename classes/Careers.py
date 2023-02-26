class Careers:
    
    def __init__ (self, careers_name):
        self.careers_name = careers_name
        self.__collection = "careers"
        
    def save(self, db):
        collection = db[self.__collection]
        collection.insert_one(self.__dict__)
        
        
        