import mysql.connector
from mysql.connector import  Error 

db_config = {
    'user': 'Martina',
    'password': '1234',
    'host':'127.0.0.1',
    'database': 'testdb'
}

try:
    db = mysql.connector.connect(**db_config)

    if db.is_connected():
        print("Connected to MYSQL database")

except Error as e:
    print(f"Error: '{e}'")


# # insert many row  #Вариант 0

# users_data = [  #Вариант 0
#     ('Pesho2', 'pesho@gmail.com'),  #Вариант 0
#     ('Pesho3', 'pesho@gmail.com')  #Вариант 0
# ]  #Вариант 0

# with db.cursor() as cursor: #Вариант 0
#     sql = f"""insert into users (name, email) values {%s, %s};""" #Вариант 0
#     print(sql) #Вариант 0
# #print(sql) #Вариант 0 
#     cursor.executemany(sql, users_data,[0]) #Вариант 0
#     db.commit()  #Вариант 0


with db.cursor()as cursor:
    sql = 'SELECT * FROM users' #Вариант 1
    cursor.execute(sql) #Вариант 1
    # while cursor.fetchone() is not None:  #Вариант 1
    #     print(sql) #Вариант 1
   
    while True:   #Вариант 2
        row =cursor.fetchone() #Вариант 2
        if row: #Вариант 2
            print(row) #Вариант 2
        else: #Вариант 2
            break #Вариант 2