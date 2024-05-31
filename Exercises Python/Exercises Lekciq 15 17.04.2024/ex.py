# OPP Examples...............

# 1.1.......................
# class A:
#     # class attribute
#     name ='A object'

#     # class method
#     def powerClass(x):
#         #  s =a1
#         # x=3
#         return x**2
    
#     # instance method 
#     def powerInstance(self,x):
#         # self=a1
#         print(f'id(self):{id(self)}')
#         return x**2


# # instatiating objects of class A
# a1 = A()
# a2 = A()

# a1.id=1
# a2.id=2



# print(a1.powerInstance(3))
# print(f'id(a1):{id(a1)}')


# show object attributes 
# print(a1.__dict__)
# print(a2.__dict__)


# read class attributes
# print(a1.name)
# print(a2.name)
# print(A.name)



# a2.foo = lambda x:x**2
# print(a2.foo(2))




# 2......................................
# Methods...................................


# Instance Method...................

# class A:
#     def instance_method(self):
#      #self = a1
#         print(self)


# a1 = A()
# a2=A()
# print(a1)
# print(a2)
# a1.instance_method()
# a2.instance_method() #object a1 , function instance_method



# 3..Examples ..................................

# class Person: 
#     def greet(self):
#         print("Hi there! i'm", self.name)

# # create some objects of class Person: 
# maria = Person()
# maria.name = 'Maria Popova'

# pesho = Person()
# pesho.name = 'Pesho'


# # call greet 
# maria.greet()
# pesho.greet()




# 4. ''Constuctor'' == __init__()method   ............................
# Дъндър Init ............................


# class A:
#     def __init__(self, id):
#         print('A constructor is called!')
#         self.id = id


# a1 = A(1)
# # a1.id = 1 - тук конструктора го прави, 
# # не се налага да го пишем, както в предния пример 
# a2 = A(2)

# print(a1.id)
# print(a2.id)




# 5.  Example __init__   ..........................


# class Person: 
#     def __init__(self, name):
#         self.name = name



#     def greet(self):
#         print("Hi there! i'm", self.name)


# # create some objects of class Person: 
# maria = Person('Maria Popova')


# pesho = Person('Pesho')


# # call greet 
# maria.greet()
# pesho.greet()



# 6. Examples for Method......

# class A:
#     x=2
#     def foo(self):
#         print('Foo')

# a = A()
# a.foo()




# 7. # ..........................................

# class A:
#     # class attributes:
#     x=2
#     # ''constructor''
#     def __init__(self)-> None:
#         pass
#     # instance method
#     def foo(self):
#         print('Foo')


# a1 = A()
# a2 = A()
# # access instance methods 
# a1.foo()

# # access class attributes
# print(A.x)
# print (a1.x)
# print(a2.x)

# Презаписване на стойност - пример /add instance..................
# a2.x = 9
# print(A.x)
# print (a1.x)
# print(a2.x)

# A.foo()




# 8. Създаване на атибути към инстанции - примери.............
# class A:
#     # class attributes:
#     x=2
#     # ''constructor''
#     def __init__(self)-> None:
#         # set instance attributes 
#         self.name = 'Anonnymous'
#     # instance method
#     def foo(self):
#         print('Foo')


# a1 = A()
# a2 = A()

# # access instance methods 
# a1.foo()

# # access class attributes
# print(A.x)
# print (a1.x)
# print(a2.x)

# # change class attributes 
# A.x=100
# print(a1.name)
# print(a2.name)




# 9. Magic Metgod - (всички с дъндър)..............................
# Example ''__str__''

# class A:
#     # class attributes:
#     x=2
#     # ''constructor''
#     def __init__(self, name)-> None:
#         # set instance attributes 
#         self.name = name

#     def __str__(self):
#         return f"name:{self.name}"


#     # instance method
#     def foo(self):
#         print('Foo')


# a1 = A('a1')
# a2 = A('a2')

# # access instance methods 
# a1.foo()

# # access class attributes
# print(A.x)
# print (a1.x)
# print(a2.x)

# # change class attributes 
# A.x=100
# print(a1)
# print(a2)


# 10. Предефиниране на оператор ...............
# Operator ovelorading .............
# Example.............
# В __self__ винаги има обект 



# class Account:
#     def __init__(self, owner, balance)-> None:
#         self.owner = owner 
#         self.balance = balance

#     def __str__(self) -> str:
#         return f'owner:{self.owner}, balance:{self.balance}'
    
#     def __gt__ (self, other):
#         return self.balance>other.balance
    
#     def __add__(self, other)->float:
#         return self.balance + other.balance


# a1 = Account('Maria', 1000)
# a2 = Account('Pesho', 200)


# # Account __gt__(a1, a2)
# # Account .__add__(a1, a2)
# print(a1+a2)

# if a1>a2:
#     print('A1 is bigger')





# 11. Inspecting objects and classes ..................         
# Inspecting - example - with __dict__


# 1.1................
# class A: 
#     x=1
#     def __init__ (self, y)->None:
#         self.y = y 

# a1 = A(9)

# print(a1. __dict__)
# print(A. __dict__)





# 12. Dir Method .............................

# class A: 
#     x=1
#     def __init__ (self, y)->None:
#         self.y = y 

# a1 = A(9)

# print(a1. __init__(a1, 9))

# # Извикваме пропъртита, които  можем да използваме 
# print(dir (a1))

# # 
# print(a1. __init__(a1))



# 13..........................
# Извикваме всички пропърти, които можем да използваме 
# .............................


# import math 

# print(dir(math))



# 14. Задачи...........
# Bank account Task: Create bank account class 

# class BankAccount:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.balance = balance 

#     def __str__(self):
#         return f"""
# BankAccount:
#     owner = {self.owner}
#     balance = {self.balance}
# """

# maria_account = BankAccount('Maria', 1_300)
# pesho_account = BankAccount('Pesho', 100)

# print(maria_account)
# print(pesho_account)





# 15.............

# class Employee: 
#     """Represents an employee with a name, Id, salary and department
#     """

#     def __init__ (self, name:str, id:int, salary:float, department:str)-> None: 
#         self.name = name 
#         self.id = id
#         self.salary = salary 
#         self.department = department 

#     def __gt__ (s,o):
#         return s.salary>o.salary



# # Create 5 employee objects with different salary 

# employees = [
#     Employee("Ivane Petrov", 123552424, 500, "Engineering"), 
#     Employee("Maria Ivanova", 25555422, 6500, "Marketing"),
#     Employee("Alisa", 565560245245, 6565, "Human Resources"),
#     Employee("aLISSA", 2325465454321, 98565632, "Finance"),
#     Employee ("Bogomilo Nikolov", 25465456435, 85622, "Finance")



# Извикваме конкретeн служител - пример.....................
# print(employees[2].name, employees[2]. salary)




# Task: print name of the Employee with highest salary........................... 
# Reshenie................


# max_salary = 0.0
# max_employee = employees[0]


# for emp in employees:
#     if emp.salary > max_salary:
#         max_salary = emp.salary
#         max_employee = emp



# Вариант едно за принтиране на заплата 
# print(max_salary)
# ...........................................



# Принтира името на служителя с най-висока заплата
# ................................................
# print(max_employee.name)



# ДРУГ ВАРИАНТ ЗА РЕШЕНИЕ............
# for emp in employees:
#     if emp.salary>max_salary:
#         max_salary = emp.salary
#         max_employee = emp




# Още еднo решение...............
# Sorted: със сориране на списък по стойностите на заплатата


# sorted_employees = sorted(employees, key=lambda emp:emp.salary)
# print(sorted_employees[-1].name)





# Решение: filtering with lest comprehensions.............................

# def variant4():
    # max_salary = max( [ emp.salary for emp in employees] )




# def variant4(): 
# 
    # max_salary = max ([emp.salary for emp in employees])
    # max_salary_employee = [emp for empp in employees if emp.salary ==max_salary][0]
    # print (max_salary_employee.name)



# Вариант 5 за решение
# Filtering with filter ...................

# def variant4(): 
#     max_salary = max ([emp.salary for emp in employees])
#     max_salary_employee = filter(lambda emp:emp. salary == max_salary, employees)
#     print(list(max_salary_employee)[0].name)

# variant4()




# 16. Call a method from method .........................
# Задача: Когато извикаме метод 1, той да извика метод 2: 


# class A: 
#     def __init__ (self, id)-> None: 
#         self.id = id 

#     def method_1(self):
#         print('method_1 is called')

#         # Call method2: 
#         self.method_2()

#     def method_2(self):
#         print('method_2 is called')


# a = A(1)
# a.method_1()



