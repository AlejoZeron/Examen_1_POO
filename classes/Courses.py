class Courses:
    
    def __init__(self, aproved_courses, reprobed_courses):
        self.aproved_courses = aproved_courses
        self.reproved_courses = reprobed_courses
        self.__collection = "courses"
        
    def save(self, db):
        collection = db[self.__collection]
        collection.insert_one(self.__dict__)
        
        
        
    