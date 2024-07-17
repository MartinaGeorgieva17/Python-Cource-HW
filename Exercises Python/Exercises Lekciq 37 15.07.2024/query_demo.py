# 1...............................


from pymongo import MongoClient
from pprint import PrettyPrinter
pp=PrettyPrinter(indent=4)

client = MongoClient('mongodb+srv://martinag17:npj3blrZbc1xaR7E@cluster0.ooxlr2a.mongodb.net/')
db = client.get_database('python_course')


# #insert data
# users_data=[
#     {
#         'name': 'George',
#         'age': 68
    
# },
# {
#     'name': 'John',
#     'age': 30
# }
# ]

# db.users.insert_many(users_data)

# # #get all documents from collection 
# documents = db.user.find()
# pp.pprint(list(documents))



# 2.......................................
#get all documents with key 'age'

# from pymongo import MongoClient
# from pprint import PrettyPrinter

# pp=PrettyPrinter(indent=4)

# client = MongoClient('mongodb+srv://martinag17:npj3blrZbc1xaR7E@cluster0.ooxlr2a.mongodb.net/')
# db = client.get_database('python_course')


# documents = db.users.find({'age':23})
# pp.pprint(list(documents))




# 3....................................

# from pymongo import MongoClient
# from pprint import PrettyPrinter

# pp=PrettyPrinter(indent=4)

# client = MongoClient('mongodb+srv://martinag17:npj3blrZbc1xaR7E@cluster0.ooxlr2a.mongodb.net/')
# db = client.get_database('python_course')


# documents = db.users.find({"age": {"$exists": True}})
# pp.pprint(list(documents))


# 4.Get all documents with age >30..........................................

# from pymongo import MongoClient
# from pprint import PrettyPrinter

# pp=PrettyPrinter(indent=4)

# client = MongoClient('mongodb+srv://martinag17:npj3blrZbc1xaR7E@cluster0.ooxlr2a.mongodb.net/')
# db = client.get_database('python_course')


# documents = db.users.find({"age": {"$gte": 30}})
# pp.pprint(list(documents))


# 5 .Get all documents with age >30 and 'name' length>4 symbols.........................................

# from pymongo import MongoClient
# from pprint import PrettyPrinter

# pp=PrettyPrinter(indent=4)

# client = MongoClient('mongodb+srv://martinag17:npj3blrZbc1xaR7E@cluster0.ooxlr2a.mongodb.net/')
# db = client.get_database('python_course')


# documents = db.users.find(
#     {
#         '$and':[
#         {"age": {'$gte':30}},
#         {'name':{"{$regex":r'.{5,}'}},
#         ]
#     }
# )
# pp.pprint(list(documents))




# 6.Update ......................................
# res=db.users.update_one(
#     {'_id': ObjectID('66916674f8fa7560272049d')}, #Въвеждаме ид-то на обекта, който ни е по система
#     {'$set':{}
#     'name':'ADA'
# }}
# )
# pp.pprint(res)


# 7.Delete..................
# Task: delete all documents, where 'password' == '12345678'
# from pymongo import MongoClient
# from pprint import PrettyPrinter

# pp=PrettyPrinter(indent=4)

# client = MongoClient('mongodb+srv://martinag17:npj3blrZbc1xaR7E@cluster0.ooxlr2a.mongodb.net/')
# db = client.get_database('python_course')
# documents = db.users.find({
#     'password': '12345678'
# })

# pp.pprint(list(documents))


# 8.........................
# Task: delete all documents, where 'password' == '12345678'
# from pymongo import MongoClient
# from pprint import PrettyPrinter
# import pymongo

# pp=PrettyPrinter(indent=4)

# client = MongoClient('mongodb+srv://martinag17:npj3blrZbc1xaR7E@cluster0.ooxlr2a.mongodb.net/')
# db = client.get_database('python_course')

# todos = db.todos.find().sort('priority', pymongo.ASCENDING)
# pp.print(list(todos))

# todos = db.todos.find(
#     {'title': {'$regex'}:r'python', '$options': 'i'}
# )
# pp.pprint(list(todos))


# 9.Search ...............................


# db.todos.create_index([
#     ('title', 'text')
# ])
# search_term = "python" 
# todos = db.todos.find({"$text": {'$search': search_term }})

# pp.pprint(list(todos))
