# Example Python Code to Insert a Document 

from pymongo import MongoClient 
from bson.objectid import ObjectId 

class AnimalShelter(object): 
    """ CRUD operations for Animal collection in MongoDB """ 

    def __init__(self,username,password): 
        # Initializing the MongoClient. This helps to access the MongoDB 
        # databases and collections. This is hard-wired to use the aac 
        # database, the animals collection, and the aac user. 
        # 
        # You must edit the password below for your environment. 
        # 
        # Connection Variables 
        #  
        HOST = 'localhost' 
        PORT = 27017 
        DB = 'aac' 
        COL = 'animals' 
        # 
        # Initialize Connection 
        # 
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (username,password,HOST,PORT)) 
        self.database = self.client['%s' % (DB)] 
        self.collection = self.database['%s' % (COL)] 

    # Create a method to return the next available record number for use in the create method
    def get_next_record_number(self):
      record=self.collection.find_one(sort=[("rec_num",-1)])
      if record:
          return record["rec_num"]+1
      return 1

    # Complete this create method to implement the C in CRUD. 
    def create(self, data):
      try:
        if data is not None: 
            data["rec_num"]=self.get_next_record_number()
            self.database.animals.insert_one(data)  # data should be dictionary    
            return True        
      except Exception as e:
        print(e)
        return False

    # Create method to implement the R in CRUD.
    def read(self,query):
      try:
          if query is not None:
              return list(self.collection.find(query))
          return []
      except Exception:
          return []

    def update(self,query,data):
      try:
          if query is not None and data is not None:
              result=self.collection.update_many(query,{"$set":data})
              return result.modified_count
          return 0
      except Exception:
          return 0

    def delete(self,query):
      try:
          if query is not None:
              result=self.collection.delete_many(query)
              return result.deleted_count
          return 0
      except Exception:
          return 0