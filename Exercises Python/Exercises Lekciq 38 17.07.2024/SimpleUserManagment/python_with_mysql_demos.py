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


# # insert many row 

# users_data = [
#     ('Pesho2', 'pesho@gmail.com'),
#     ('Pesho3', 'pesho@gmail.com')
# ]

# with db.cursor() as cursor:
#     sql = f"""insert into users (name, email) values {%s, %s};"""
#     print(sql)
# #print(sql)
#     cursor.executemany(sql, users_data,[0])
#     db.commit()


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