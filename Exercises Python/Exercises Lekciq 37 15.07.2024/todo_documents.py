import pymongo 
from datetime import datetime
from pymongo import MongoClient
from pprint import PrettyPrinter

pp=PrettyPrinter(indent=4)

client = MongoClient('mongodb+srv://martinag17:npj3blrZbc1xaR7E@cluster0.ooxlr2a.mongodb.net/')
db = client.get_database('python_course')

# res = db.todos.insert_many([
#     {
#         'title': 'Learn Python',
#         'completed': True,
#         'dueDate': datetime.fromisoformat("2021-07-12"),
#         'priority':1
#     },
#     {
#         'title': 'Learm Flask',
#         'description': 'Learn Flask to develop quick annd easy web application with ability to scale up',
#         'completed': True,
#         'dueDate': datetime.fromisoformat("2022-01-12"),
#         'priority':2
#     },
#     {
#         'title': 'LearnMongoDB',
#         'completed': False,
#         'dueDate':datetime.fromisoformat("2022-01-12"),
#         'priority':1
#     }
# ])

# print(res.inserted_ids)





# 2.Task: Get all ...............................


# todos = db.todos.find().sort =('priotirity', pymongo.ASCENDING)
# pp.pprint(list(todos))



# 5. Get all todos, where 'dueDate'>2021-12-01...............................
# date_obj = datetime.fromisoformat("2021-12-01")
# new_todos = db.todos.find({"dueDate"}:{"$gt":date_obj}})
# pp.pprint(list(new_todos))


# 6..............................
# todos = db.todos.find({}, {'_id':0, 'title':1})
# pp.print(list(todos))


# 7.Print only the titles.................
# todos = db.todos.find({}, {'_id':0, 'title':1})
# for todo in todos:
#     print(todo['title'])




# 8.................................
