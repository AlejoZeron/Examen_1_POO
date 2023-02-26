from classes.DbMongo import DbMongo
import pymongo
from dotenv import load_dotenv
from classes import DATA, Dataprocess, Students, Careers, Courses, Enrollments

def main():
    
    client, db = DbMongo.getDB()
    
    pipeline = Dataprocess(DATA)
    
    pipeline.create_careers()
    pipeline.create_students()
    pipeline.create_enrollments()
    

    return True
    
    client.close()
    
if __name__ == "__main__":
    load_dotenv()
    main()