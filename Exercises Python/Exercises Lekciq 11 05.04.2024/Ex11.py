#от лекция 10 
# l = [1,2,3]
# print(type([el**2 for el in l])) #list comprehension

# print(type({el**2 for el in l})) #set comprehension

# print(type((el**2 for el in l))) #generator comprehension

# #Lazy evoluation/generator comprehension
# for x in (el**2 for el in l):
#     print(x)


#1. Модули и пакети ..................
# print ('hi')

# #built-in module

# import itertools
# import math 

# for c in itertools.count(10):
#     print(c)




#2 .Модули .....................

# print ('hi')
# import itertools
# import math
# print(math.remainder(5,2))
# print(5/3)



# 2.2. Модули /import module namespace.........................

# print ('hi')
# import itertools
# import math
# print(math.remainder(5,2))
# print(math.floor(2.1))
# print(math.ceil(2.1))
# print(round(2.6666668, 2)) # do vtora cifra zakruglq 


# print(math.pi)



#3. Import functions friom module ..................................
# import itertools
# import math

# from math import pi, floor
# print(pi)
# print(floor(2.99999))



#3.1. Използване на псевдоним aliase/Import module aliase.........................

# import itertools as it 
#прекръстваме функцията 



# 4. Създаванена модул  ...................
# създаваме функция първо 

# def input_number():
#     while True: 
#         try:
#             x=int(input('Enter a number: '))
#             break; 
#         except:
#             print('Please, enter a number!!!')
  
# input_number()

# print('my lib is executed')
# x=1

# #Взимаме горната част и създаваме наш модул с нея в нов файл вместо да я пишем отново и отново
# В случая използваме my lib и извикваме с нея цялата горна част
# В новият файл ще можем по този начин да използваме информацията в горната част 
# #custom module

# import mylib
# mylib.input_number()




#5. .......................

# def input_number():
#     while True: 
#         try:
#             x=int(input('Enter a number: '))
#             break; 
#         except:
#             print('Please, enter a number!!!')
  
# def input_float():
# print('input float..')
# input_float()






# def greet():
#     print('Greeting')

# greet()


# # Вариант едно за за извикване на метода ...................
# import user_output as uo
# uo.greet()


# # Вариант две за за извикване на метода..............
# from user_output import greet 
# greet()


# # Вариант три за извикване на метода
# import user_output as user_output
# user_output.greet()





# 6. Извикаваме останлите методи, които сме създали по следния начин ...........................

# import lib.io.user_output 

# Вариантът е валиден при положени, че имаме папка с име lib/io и папки 
# user_output и user_input, main и тн /NEW FOLDER MY PROJECT с изброените файлове new file в тях 


# from lib.io.user_output import greet 
# greet()





# 7. __name__   /variable ..........................................................


# def input_number():
#     while True: 
#         try:
#             x=int(input('Enter a number: '))
#             break; 
#         except:
#             print('Please, enter a number!!!')
  
# def input_float():
#     print('input float..')
# input_float()

# print(__name__)


# when imported as module ............
# 'lib.io.user_input'




