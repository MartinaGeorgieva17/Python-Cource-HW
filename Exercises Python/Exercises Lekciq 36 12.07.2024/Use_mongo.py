# 1......................................
# from pymongo import MongoClient

# uri = "mongodb+srv://martinag17:npj3blrZbc1xaR7E@cluster0.ooxlr2a.mongodb.net"
# client = MongoClient(uri)

# dbs=client.list_database_names()
# print(dbs)



# 2.......................


# from pymongo import MongoClient

# def connect_to_local_server():
#     connection_string = "mongodb://localhost:27017/"  # Примерен connection string за локален MongoDB сървър
#     return MongoClient(connection_string)

# def connect_to_atlas_cluster():
#     connection_string = "mongodb+srv://martinag17:npj3blrZbc1xaR7E@cluster0.ooxlr2a.mongodb.net/"
#     return MongoClient(connection_string)

# atlas_client = connect_to_atlas_cluster()
# local_client = connect_to_local_server()

# print(atlas_client.list_database_names())
# print(local_client.list_database_names())





# 3.Connect to mongo server ........................................
# from pymongo import MongoClient

# client = MongoClient("mongodb+srv://martinag17:npj3blrZbc1xaR7E@cluster0.ooxlr2a.mongodb.net/")


# print(client.list_database_names())




# 4..List collections in a data base ...................................................

# from pymongo import MongoClient

# client = MongoClient()
# db = client.python_course
# res = db.users.insert_one ( {
#         "name": "Mariq",
#         "password":"1234"
#     }
# )

# print(f"Doc Id:{res.inserted_id}")




# 5.Получаваме информация за всички документи в Mongo..........................
# from pymongo import MongoClient

# client = MongoClient()
# db = client.python_course
# all_docs = db.users.find()
# print(all_docs)



# 6.Получаваме информация за всички документи в Mongo като лист.............................
# from pymongo import MongoClient

# client = MongoClient()
# db = client.python_course
# all_docs = db.users.find()
# print(list(all_docs))





# 7.Get user by name..................................

# from pymongo import MongoClient

# client = MongoClient()
# db = client.python_course
# db.users.find({"name":"Ada"})
# print(list(users))




# 8....................................
# from pymongo import MongoClient

# client = MongoClient()
# db = client.python_course
# users = db.users.find(
#     {"name":"Ada"}, 
#      {"id":0,
#       "password":1
#      }
# )
# print(list(users))



# 9........................


