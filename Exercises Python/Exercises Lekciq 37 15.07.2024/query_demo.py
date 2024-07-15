from pymongo import MongoClient

client = MongoClient('mongodb+srv://martinag17:npj3blrZbc1xaR7E@cluster0.ooxlr2a.mongodb.net/')
db = client.get_database('python_course')

#get all documents from collection 
documents = db.user.find()
print(list(documents))
