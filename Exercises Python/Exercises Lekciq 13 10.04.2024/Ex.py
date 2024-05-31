# Упражнения върху функции


# 1. Scope /Обхват на прменливи ......................
# Глобален / Global/
# Global Scope е само тялото на функцията, като цъкнем стрелкичката се скрива останалата част
# ... но останалата, която е видима е Global !!!!


# Пример за глобален и локален скоуп 



# def foo():
#     x=9 #(локален скоуп)

# x = 1 #(глобален скоуп)
# foo()
# print(f'x in global:{x}')




# 1.2. Пример ................


# def foo():
#     x=5
#     print(f'x in foo:{x}')

# def bar (x):
#     print(f'x in bar:{x}')

# x = 1 
# foo()
# bar(9)
# print(f'x in global:{x}')




# 1.3...............................
# Припомняне модули / Извън темата

# def greetAda():
#     userName='Maria'
#     print(f'Hello {userName}')

# if __name__=='__main__':
#     userName = 'Ada'
#     greetAda()


# # ИМПОРТВАНЕ НА МОДУЛА .................

# import lib 

# lib.greetAda()





# 2. Global Scope Example ......................................
# Задачаа: 
# number = 1
# def increment():
#     number+=1

# increment()


# # Решение: ....................

# number = 1

# def increment():
#     global number
#     number += 1

# increment()
# print(number)  # Изход: 2


# # Второ решение: ..................

# number = 1

# def increment(num):
#     return num + 1

# number = increment(number)
# print(number)  # Изход: 2




# 3. In-Place Arguments/ ..........................................
# Pass value vs pass References

# Pass Value Example


# def foo(x):
#     x=100
#     print(y)
#     print(x)

# y = 1
# foo(y)
# print(f'y in main: {y}')




# 3.1.Пример Две /pass References for all mutables types........................................................
# При извикване на функция дава адреса на паметта 
# 


# def foo(x):
#     x[0]=100
#     print(y)
#     print(x)

# y = [1]
# foo(y)
# print(f'y in main: {y}')




# 4.Анонимна / Lamba функция......................
# Задача да върне 8 


# def cub(x):
#     return x**3

# x = 2
# print(cub(x))  
# print(x)




# 4.1.  Задачата, но с lamba .........................

# def calc(f,c):
#         print(f'Calculating...')
#         #  f = cub 
#         return f(x)


# def cub(x):
#     return x**3

# def power(x):
#       return x**2

# x = 2
# print(calc(cub, x))  
# print(calc(power, x))
# print(x)


# .......................................

# def calc(f,c):
#         print(f'Calculating...')
#         #  f = cub 
#         return f(x)

# cub = lambda x:x**3

# x = 2
# print(calc(lambda x:x**3,x))  
# print(calc(lambda x:x**3,x))
# print(x)




# 4.2..........................
# Задача : Use case 1: sort list of dictionaries
# Sort students by math score 



# students = [
#     {
#         'name' : 'Ivan',
#         'math': 5,
#         'physics': 4
#     }, 
#     {
#         'name': 'Maria', 
#          'math': 6,
#         'physics': 3
#     }, 
#     {
#         'name': 'Petar ', 
#          'math': 4,
#         'physics': 6
#     }
# ]





# ...............................................

# Решение Едно:

# def sort_by_math(student):
#     return student['math']


# students.sort(key=sort_by_math)
# print(students)





# .....................................

# Вариант две за крайно решение на заачата с LAMBA:..........

# def sort_by_math(student):
#     return student['math']


# students.sort(key=lamba student:student['math'])
# print(students)

# ......................................................




# *Преговор за Sorted....................

# l=[5,6,4]

# l.sort

# print(l)

# .......................................






# 4.3. Пример за използване на lamba .......................

# def foo(x,y):
#     return x+y

# bar = lambda x,y:x+y 

# print(bar(2,3))
# print(foo(2,3))





# 4.4 Lampda Exersise ...............................

# l = [5, 6, 4]

# def filteredby_value(el):
#     if el > 4:
#         return True
#     else:
#         return False

# filtered = filter(filteredby_value, l)
# print(list(filtered)) 





# 4.5 Lampda Exersise ...............................
# Task: filter students by math score > 4


# students = [
#     {
#         'name' : 'Ivan',
#         'math': 5,
#         'physics': 4
#     }, 
#     {
#         'name': 'Maria', 
#          'math': 6,
#         'physics': 3
#     }, 
#     {
#         'name': 'Petar ', 
#          'math': 4,
#         'physics': 6
#     }
# ]

# Example 1 the worst .........................

# filtered = []
# for student in students:
#    if student['math']>4: 
#      filtered.append(student)

# print(filtered)




# Вариант две за решение:/ with filter .............................
# filtered = filter(lambda student:student['math']>4, students)
# print(list(filtered))




# Вариант три за решение:/ list comprehensions ........................

# filtered = [student for student in students if student['math']>4]
# print(filtered)




# 4.6...........................................

# Task: map students to student_names 



# students = [
#     {
#         'name' : 'Ivan',
#         'math': 5,
#         'physics': 4
#     }, 
#     {
#         'name': 'Maria', 
#          'math': 6,
#         'physics': 3
#     }, 
#     {
#         'name': 'Petar ', 
#          'math': 4,
#         'physics': 6
#     }
# ]



# Вариант едно за решение /Най-лошият:..........................

# student_names = []
# for student in students: 
#     student_names.append(student['name'])

# print(student_names)




# Вариант две за решение:/with map function  ...........................

# student_names = map(lambda student:student['name'], students)
# print(list(student_names))






# Вариант три за решение/ with list coprehensions...................................

# student_names =[student['name'] for student in students]
# print(student_names)







# 5. Рекурсивна функция  -извиква сама себе си (Factoriel).....................

# def foo(n): 
#     print('Foo is called')
#     if n>0:
#         foo(n)
#         n-=1
#         foo(n)
#     else:
#         return None

# foo(5)




# 5.1 Use Case..........................................................
# Task: Calculate Factoriel (N)
# Правила:.........
# factoriel(n):
# n==1 => 1
# n>1 => n.factoriel(n-1)




# .Задача: ......................

# def factoriel(n):
#     if n ==1:
#         return 1
#     else:
#         return n*factoriel(n-1)
    
# print (factoriel(3) )




# 5.2 Типизиране на функция: ..................

# def add(x:int, y:int)->int:
#     return x+y

# add(2,3)



# 6....................................
# Cerate a program that reads integers entered by the user. 
# until an empty line is entered. After all the numbers have been read, the program
# should display all negative numbers followed by zeros followed by alls positive numbers 
# In each group the numbers must appear in the same order , c which are entered by the yser
# For example, if the user enters the values: 3, -4,1,0,-1, 0 and - 2
# your program should output the values -4,-1,-2,0,0,3 and 
# your program should display each value on a new 



