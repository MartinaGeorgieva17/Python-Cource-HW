#print(bool(''))
#print (bool('-0.00000000'))
#print (bool('-000000000.1'))

##Logical AND (and)

#1
#print (2+2)
#print ( 2 or 3)

#2
#user_age = 19
#country = 'BG'

#if user as adult in is from Bulgaria 
##  print('Welcome')

#4
#print (True and False)
#print (False and False)
#print (True or True)

#5 Logical OR
#print(False or False) #False
#print(False or True) #True 
#print(True or False) #True 
#print(True or False) #True

#6
#if user as adult or is from EN => say Welcome

#user_age = 19 
#country = 'BG'

#if user_age>=18 or country=='En':
#    print('WElcome')


#7Logical NOT
#7.1
#print( not True)
#print( not False)

#7.2
#print(not 2) 
#print(not'')

#7.3
#print(True and False) #F
#print(False and True) #F
#print(False and False) #F
#print(FTrue and True)  #

#print(2 and 0) #0
#print(0 and 2) #
#print ('' and 3.5-2.5-0.5) #''

#7.4
#user_name = ''

###if not user_name:
   # user_name = 'Annonymous'
    
   # print(user_name)


#7.5
#user_name = 'Ada'

#user_name and (user_name := 'Anno')

#print(user_name)



#7.6 Logcal OR

#user_name = 'Ada'

#user_name or (user_name := 'Anno')

#print(user_name)


#7.7 Sravnqvane 

#print(9<1000) #True 
#print('9' < "1000") #False kogato se sravnqvat kato stringove ASCii TABLE 
#print('a'<'A') #vzima cifrite ot stringovete ot ASCII TABLE i stava 97<65

#7.8 Comparision 
#user_age = 0

#if not 0<user_age<120:
 #   print('Unvalid user age')

#7.9 Pass 
##user_age = 0
#if not 0<user_age<120: # sled dvete tochki Pythonochakva statement
#ne moje da ima prazen blok sled :
   # pass #mojem v takiva sluchaai da izpolzvame pass
#print('End')

#7.10 Ternary Operator 

#conditional_expression = <expr> if value1 else value2

#user_age = 19 
#user_status = ''

#if user_age>=18:
  #  user_status = 'adult'
#else: 
  #  user_status = 'Child'

#print(user_status)

#variable = value1 if <expr> ielse value2

#user_age = 19 

#user_status = 'Adult' if user_age>=18 else "Child"

#print(user_status)


#7.11 Ternary Operator 

#x = 2 if 4>5 else 1

#print(x) #1

#7.12 Ternary Operator 

#if 2 if 4>5 else 1:
  #  print('Hi')

#8.00 Zadachi 

#computer_number = 5

#[1, 10]

#3 => '3 is less'
#8 => '8 is higher'


#from random import randint


#computer_number = randint(1,10)
#print(f'(computer_number={computer_number}')


#user_number = int(input('Enter a nmuber:'))
#print(f'user_number = {user_number}')

#if user_number == computer_number:
 #   print('Bravo')
#elif user_number < computer_number:
 #   print('your guess is less than my number. Try again')
#else:
 #   print('Your guess is great than my number. Try again')



#BMI - examples operatori za sravnqvane

weight = 87 
height = 1.78

bmi = weight/height**2
print(f'BMI:{bmi}')


if bmi <= 18.5:
    print('YOU ARE underweight')

elif 18.5<bmi<=24.9:
    print('You are Normal')

elif 25<bmi<=29.9:
    print('You are Overweight')

elif bmi>=30:
    print('You are Obesity')

else:
    print('Strange case')
