class Enrollments:
    
    def __init__(self, date_inscription):
        self.date_inscription = date_inscription
        self.__collection = "enrollments"
        
    def save(self, db):
        collection = db[self.__collection]
        collection.insert_one(self.__dict__)
        
        
        