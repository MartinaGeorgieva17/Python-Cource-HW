# inheritance - наследяване ............................
# 1.................................................



# class Person: 
#     def __init__ (self, name, age)-> None: 
#         self.name = name 
#         self.age = age 
    
#     # Добра практика да има str 
#     def __str__(self):
#         return f"name={self.name}, age:{self.age}"



# # Ако искаме да променим името, атрибут на даден обект, трябва ни метод
# # setters
#     def setName(self, new_name):
#         self.name = new_name
# # getters
#     def getAge(self):
#         return self.name


# # Може да има и определени действия, които да се изпълняват като: 

#     def greet(self):
#         print(f'Hello, im {self.name}, {self.age}, years old!')


# # Student is a person .- Наследяването се осъщестявва в случая със ()
# # Добавили сме (Person)

# class Student(Person): 
#     def __init__ (self, name, age)-> None: 
#         self.name = name 
#         self.age = age 
#         self.courses = []

# # Опция към студентите, което могат да направят: 
#     def enroll_class(self, course_name):
#         self.courses.append(course_name)

# # Ovrride - ако има собствен метод се изпозлва него, но ако няма излиза Hello 
#     # def greet(self): 
#     #     print('Hello')


#     # Как в един клас наследник да извикаме метод от родителския клас
#     # Пример към задачата



# class Teacher: 
#     pass


# pesho = Student('Pesho', 23)
# pesho.enroll_class('Python')
# pesho.greet()




# Решение (викане без klasove student и teacher):

# person1 = Person('pesho', 23) # Решение (викане без klasove student и teacher)
# person1.setName('Petar')  # Решение (викане без klasove student и teacher)
# print(person1)






# ..............................................................
# 2.    # Как в един клас наследник да извикаме метод от родителския клас
    # Пример към задачата...........................................................


# class Person: 
#     def __init__ (self, name, age)-> None: 
#         self.name = name 
#         self.age = age 
    
#     # Добра практика да има str 
#     def __str__(self):
#         return f"name={self.name}, age:{self.age}"



# # Ако искаме да променим името, атрибут на даден обект, трябва ни метод
# # setters
#     def setName(self, new_name):
#         self.name = new_name
# # getters
#     def getAge(self):
#         return self.name


# # Може да има и определени действия, които да се изпълняват като: 

#     def greet(self):
#         print(f'Hello, im {self.name}, {self.age}, years old!')


# # Student is a person .- Наследяването се осъщестявва в случая със ()
# # Добавили сме (Person)

# class Student(Person): 
#     def __init__(self, name, age): 
#         super().__init__(name, age)
#         self.courses = []

# # Опция към студентите, което могат да направят: 
#     def enroll_class(self, course_name):
#         self.courses.append(course_name)

# # Ovrride - ако има собствен метод се изпозлва него, но ако няма излиза Hello 
#     def greet(self): 
#         Person.greet(self)
#         print('And Im a student!')


# class Teacher: 
#     pass


# pesho = Student('Pesho', 23)
# pesho.enroll_class('Python')
# pesho.greet()






# 3. super().........................................



#     class Person: 
#     def __init__ (self, name, age)-> None: 
#         self.name = name 
#         self.age = age 
    
#     # Добра практика да има str 
#     def __str__(self):
#         return f"name={self.name}, age:{self.age}"



# # Ако искаме да променим името, атрибут на даден обект, трябва ни метод
# # setters
#     def setName(self, new_name):
#         self.name = new_name
# # getters
#     def getAge(self):
#         return self.name


# # Може да има и определени действия, които да се изпълняват като: 

#     def greet(self):
#         print(f'Hello, im {self.name}, {self.age}, years old!')


# # Student is a person .- Наследяването се осъщестявва в случая със ()
# # Добавили сме (Person)

# class Student(Person): 
#     def __init__ (self, name, age)-> None: 
#         super().__init__(name, age)
#         self.courses = []

# # Опция към студентите, което могат да направят: 
#     def enroll_class(self, course_name):
#         self.courses.append(course_name)

# # Ovrride - ако има собствен метод се изпозлва него, но ако няма излиза Hello 
#     def greet(self): 
#         super().greet()
#         print('And Im a student!')


# class Teacher: 
#     pass


# pesho = Student('Pesho', 23)
# pesho.enroll_class('Python')
# pesho.greet()







# 4...............................
# Как да направим така че атрибутът да е недостъпен от всеки 
# Не можем!!!....................................
# По-скоро само го маркираме, но може да бъде променен, 
# дори и да сложим __ (двойна подчертавка).


# class A: 
#     def __init__ (self, id) -> None:
#         self.__id = id 


# a = A(1)
# a.__id = 2 
# print(a.__id)


# Модул за операционна система
# /OS module/Basic Concepts:Paths and current working Directory
# 





