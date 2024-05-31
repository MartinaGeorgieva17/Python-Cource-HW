my_integer = 25
first_name = "Martina"
# String (низ от символи)
my_string = "Python 2024"
# Boolean (логическа стойност)
my_boolean = False
# Float (дробно число)
num1 = 0.5
num2 = 0.6
# Изчисление с дробни числа
result = num1 + num2

# Datetime (дата и час)
import datetime
my_datetime = datetime.datetime.now()

#Принтиране на стойностите
print("Age:", my_integer)
print("Name:", first_name)
print("Course:", my_string)
print("Is married:", my_boolean)
print("Date:", my_datetime)
print("Result of data from the course:", result)


#Задача 4
# Присвояване на стойности на променливи
x = 3
y = 10

# Изчисляване на резултат
result = x + y

# Извеждане на резултата с f стринг
print(f"{x} + {y} = {result}")


#Задача5
# Дефиниране на височина и база
height = 13.66  # височина в см
base = 245.54  # срещуположната страна в см

# Изчисляване на лицето на триъгълника
area = 0.5 * base * height

# Извеждане на резултата
print("Лицето на триъгълника е:", area, "кв. см")

#Задача6
# Деклариране на променливи за данните на служителя
first_name = "Dimitar"
last_name = "Georgiev" 
age = 20
gender = "male"
unique_id = 588

# Извеждане на информацията за служителя
print("Name:", first_name)
print("Last Name:", last_name)
print("Age:", age)
print("Employee Id:", unique_id)

#Задача 7
# Деклариране на променливи и задаване на стойности
num1 = 5
num2 = 10

# Извеждане на оригиналните стойности
print("Първо число (преди размяна):", num1)
print("Второ число (преди размяна):", num2)

# Размяна на стойностите
temp = num1
num1 = num2
num2 = temp

# Извеждане на новите стойности след размяната
print("Първо число (след размяна):", num1)
print("Второ число (след размяна):", num2)

#Задача 8 
# Въвеждане на дължина и височина на успоредника
length = float(input("Въведете дължина на успоредника: "))
height = float (input("Въведете височина на успоредника: "))

# Изчисляване на периметъра и лицето 
perimeter = 2* (length + height)
area = length * height 

#Резултат 
print("Периметърът на успоредника е", perimeter)
print("Лицето на успоредника е", area)

#Задача 9 
# Въвеждане на стойности за страните на триъгълника
import math
a = float(input("Въведете дължината на страна a:"))
b = float(input("Въведете дължината на страна b: "))

# Пресмятане на хипотенузата (c) с помощта на Питагоровата теорема
c = math.sqrt(a**2 + b**2)

# Отпечатване на резултата
print("Хипотенузата (c) е:", c)

#Задача 10 
import math
# Въвеждане на радиуса на кръга
radius = float(input("Въведете радиуса на кръга: "))

# Пресмятане на лицето на кръга
area = math.pi * radius**2

# Отпечатване на резултата
print("Лицето на кръга е:", area)

#Задача 11
# Въвеждане на дължина в инчове
x_in_inche = 10
x_in_cm = x_in_inche * 2.54 

print(x_in_cm)

#Упражнения за capitalized урок 3
user_surname = 'GeOrgieva'
print(user_surname.capitalize())
user_surname = user_surname.capitalize()
print(user_surname)

#Подравняване на текст 
text = 'abc'
print(text)

#print('text.center(10))

#Concatenatitio за повторение 
text = 'abc' 
text = text * 10 
text *=10

print(text) #принтира се повторение на текста
 
#f strings упражнения 
#първо упражнение без f string 
user_name = "Adi"
print( 'Hello' + user_name + '!')

#Вариант 2 с f стринг 
user_name = "Adi"
print(f'Hello {2+2}!')

#Упражнение string.format() method 
x = 5 
y = 10 
result = x+y
print('{}+{}={}'.format(x,y, result))
print('{}+{}={}'.format(1,2,3))

#Ако искаме да видим закръглен резултат 
#budget = 1000
#print(budget/12)

print('{:.2f}'.format(83.365265))
print('{%.2f' % value)
print(f'{value:.2f}')

#Задача 2 - урок 3 с f STRING 

name = 'Димитър'
sport = 'tenis'
#print("{2}'s favourite sports is {2}".format(name, sport))
#print(f"{name}'s favourite sports is {sport}")

#Format aligned
#|---name---|---age---|
#|---Nadq---|---age---|

#x = 1
#print(f'|{x:10}|')
#print(f'|{x:<10}|')

#|---name---|---age---|
#|---Nadq---|---age---|

#title method 
user_name = 'ada Guhkuhul'
print(user_name.title())

#За смяна на пурва буква сглавна или малка 
user_name = 'ada Guhkuhul'

print(user_name.upper())
print(user_name.lower())

#Replace method 
#replace a with @ in text 

text = 'abala'
print(text.replace('a', '@'))

#Ако искаме да заместим само първите две а-та 
text = 'abala'
print(text.replace('a', '@', 2))

#find method /показва конкретните символи от текста 
text = "abc"
print(text[0])
print(text[2])

#
text = 'this is apple'
print(text.find("apple"))
#получаваме индексът от където започва apple

#split method 
text = "one two three"
words = text.split(" ")

print(words)
for word in words: 
    print(f"{word}-{len(word)}")

    #Втори вариант за split method 
text = "1-2-3"
print(text.split("-"))





