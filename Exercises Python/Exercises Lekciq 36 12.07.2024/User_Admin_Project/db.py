from pymongo import MongoClient

class DB:
    def __init__(self, connstr="mongodb://localhost:27017") ->None:
        try: 
            #client =MongoClient
            self.client = MongoClient("mongodb+srv://martinag17:npj3blrZbc1xaR7E@cluster0.ooxlr2a.mongodb.net/")
            self.python_course_db = self. client.gt_database("python_courses")
        except: 
            print("Can not connect to server!")

    def list_collections(self, db_name):
        db=self.client[db_name]
        print(db.list_collestion_names())

    def insert_user(self, name, passwd):
        #db_name ="python_course"
        #collections = "users"


        try:
            res = self.python_course_db.user.insert_one({
            "name": name, 
            "password":passwd
        })
            
            return res
        except Exception as e:
            raise(e)


         # document1 = {
        #     "name":"Martina",
        #     "password": 1234
        # }