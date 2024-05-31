# Какво представляват функциите?................
# Разбиваме задачата на подзадачи 
# Спестяват писането на код
# Procedural Programming 



#1........................
# def sub_task1(): 
#     pass

# def sub_task2(): 
#     pass

# def sub_taskN(): 
#     pass

# main program .......
# sub_task1
# sub_task2
# sub_task3


# 2.Синтаксис на функция..................

# user_name = 'Ada'
# print('*'*50)
# print(f'Hello, {user_name}')
# print('*'50)

# user_name = 'Martina'
# print('*'*50)
# print(f'Hello, {user_name}')
# print('*'50)

# ..................................
# Можем да направим списък 
# За да стане по-четим създаваме функция по-следния начин от горни пример 
# ....................................

# def greet():
#     print('*'*50)
#     print(f'Hello, {user_name}')
#     print('*'*50)


# user_name = 'Ada'
# greet()

# user_name = 'Martina'
# greet()




# 3. User Defined Function UDF и Build-in.............................


#4.Какво са параметри на функции ............................
# В нашия пример - greet()
# user_name = 'ada'

# def greet(user_name):
#     print('*'*50)
#     print(f'Hello, {user_name}')
#     print('*'*50)


# greet('Ada')
# greet('Martina')




# 5. Предаване на повече от един параметър с функция..............................

# def add(x,y):
#     # x=1
#     # y=2
#     print(x+y)

# add(1,2)



# 6. Предаване на списък като параметър/List as argument .....................

# def sum_list(x):
#     print(sum(x))

# l = [1,2,3]
# sum_list(l) 
# ..................

#Втори пример: ...................
# ...........................
# def print_last(l):
#     print(l[-1])

# print_last([1,2])



# 7. Предаване на Dictionary като параметър/Dictionary as argument  ...................................

# def print_data(d): 
#     print(f'name:{data["name"]}, age:{d["age"]}')

# data = {
#     'name':'Ada',
#     'age':23
# }

# print_data(data)

# print_data(data['name']) # print с key при dictionary 
# при викане на функцията очакваме да видим NAME:ADA, AGE: 23 - СТРИНГ 



#8. Параметри по подразбиране/Default Parameters  ............................

# def foo(x=100): #ако не се подаде стойност изкарва директно 100
#     print(x)

# foo(1)
# foo()


# 8.1 Пример две:.................

# def greet_user(name='Anonuymous'):
#     print(f'Hello, {name}')

# greet_user('Ada')
# greet_user()



#8.3 Пример три: ...........................

# def greet_user(age, name='Anonuymous'):
#     print(f'Hello, {name}. You are {age} yeaars old')

# greet_user(23, 'Ada')
# greet_user(34)




#8.4 Пример Четири:.......................

# def bar(x, y= 1, z=1):
#     print(x,y,z)

# bar(1,2,3)
# bar(1,2)
# bar(1)



#9. Незадължителни параметри на функции .....................

# def print_name(first,  last, middle=''):
#     print(f'{first} {middle} {last}')

# print_name('Ada', 'Brown')
# print_name('Maria', 'Ivanova', 'Blq')




#10. Присвояване на стойност на параметри/Keyword Arguments........................

# def print_user_data(name, age, town, height):
#     print(name, age, town, height)

# print_user_data('Ада', 23, 'София', 134)
# print_user_data(
#     age=23, 
#     height=134, 
#     name='ada', 
#     town='sofiq'
# )




# 10.1 Пример две: ...........................

# def foo(x, y, z=1):
#     print(x,y,z) #x2, y=1, z==1

# # positional arguments......
# foo(1,2,3)

# # keyword arguments.....
# foo(y=1, x=2) 






# 10.2 Пример Три: ..................................

# def foo (x, y=1, z=2):
#     print(x,y,z)

# foo(1, z=99, y=4)






#10.3 Пример Три за хвърляне на грешка, защото повратяме цифрите а и б ........................

# def foo(a,b,c,d):
#     #a=1; b=2; error
#     print(a,b,c,d)

# foo(1,2,a=1, b=2)


#ПРАВИЛНО РЕШЕНИЕ на горния пример: 
# def foo(a,b,c,d):
#     #a=1; b=2; error
#     print(a,b,c,d)

# foo(1,2,c=1, d=2)





# 11. Предаване на параметри като *args (събира всички positional arguments)...............................

# def add(*args):
#     #args = (2, 3)
#     print(args)
#     print(f'sum={sum(args)}')

# add(2)
# add(2,3)
# add(1,2,3)
# add(1,2,3,4)






#11.1 Втори пример: ...............

# def foo(x,y, *args):
#     #x=1, y=2, args = (3,4,5) тъпъл (скобите)
#     print(x,y,args)

# foo(1,2,3,4,5)






# 11.2 Пример Три: .......................................
# Хвърля грешка..........


# def foo(*args):
#     print(args)

# foo(1,2, x= 3)





# 12. Предаване на параметри като **kwargs ..................................

# def foo(**kw):
#     #kw ={}
#     print(kw)

# foo()





# 12.1. Пример ..................

# def foo(**kw):
#     #kw ={}
#     print(kw)

# foo()
# foo(x=1)
# foo(x=1, y=2)





#12.2. Пример:  ...........................

# def sum_values(**kw):
#     print(sum(kw.values()))

# sum_values(x=1, y=2) #3
# sum_values(x=1, y=2, z=3) #6





# 13. Връщане на стойност/ Return Value...........................

# def add(*args):
#     print(f'sum ={sum(args)}')
#     return sum(args)

# res = add(1,2) **2; #1+2 na втора степен и получаваме 9.............
# print(res) #9





# 13.2 Пример Две: .............

# def add(x,y):
#     print(f'sum ={x+y}')
#     return x+y #каквото напишем след return това връща 

# res = add(1,2) **2; #1+2 na втора степен и получаваме 9.............
# print(res) #9





# 13.3 Трети пример: .....................

# def foo():
#     return 5 

# res = foo() + foo() # 5+5 = 10 отговор ..............
# print(res)





# 13.4. Пример Четири ...................

# def foo():
#     print('Foo')
# res = foo()
# print(res)





# 13.5 Пример Пет:   .............................


# def foo(x):
#     return x**2

# print(foo(2)+3) #Две на втора + 3 = 7 





# 13.6 Пример Шест .  .........................
# def foo(x):
#     res = x**2
#     print(f'res = {res}')
#     return x**2

# print(foo(2)+3) #Две на втора + 3 = 7 

# # Отговор: res = 4 
# # 7



# 14. Ternary Operator .........
#Припомняне ......................
# user_age = 17  
# status = ''
# if (user_age>=18):
#     status = 'adult'

# else: 
#     status = 'child'

# print(status)

# user_age = 17  
# status = 'adult' if user_age>=18 else 'child'
# print(status)
# ......................................





# ПРИМЕР.Едно.................................

# def user_status(age):
#     if age>=18:
#         return 'adult'
#     else: 
#         return 'child'

# print(user_status(21)) #adult
# print(user_status(13)) #child 



# СЪкратен и по-правилен пример на задачата .........................................

# def user_status(age):
#    return 'adult' if  age >=18 else 'child'

# print(user_status(21)) #adult
# print(user_status(13)) #child 




# 15.Scope/ Пример едно: ........................


# def foo(x):
#     print (x+1)

# x = 1
# foo(5)





# 15.1 Пример две: .................................

# def foo():
#     x=3
#     print (x)

# x = 1
# foo()
# print(x)




# def foo():
#     x=3
#     print (x)


# x = 1
# foo()
# print(x)




#16.Примери/Списъци ..............
# Трябва да разменим стохйостите в две променливи 

# x= 1 
# y = 2

# tmp = x
# x=y
# y=x

# print(x,y)



# Второ решение: 
# x, y = y,x 


# 16.1.................

# x,y,z = [1,2,3]
# print(x,y,z)




