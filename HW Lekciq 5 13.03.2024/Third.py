#Съставете програма, която по въведено трицифренo число проверява дали числото се дели на всяка своя цифра. Във въведеното число да няма цифра 0. Използвайте проверка на логическо условие - оператор if.
#Пример: 121 Изход: 1:2:4 дели се


# Въвеждане на трицифрено число от потребителя
number = int(input("Въведете трицифрено число без цифарата 0:"))

# Проверка дали въведеното число е трицифрено и не съдържа 0
if number >=100 and number <=999 and '0' not in str(number):
        # Извличане на цифрите на числото
    units = number%10
    tens = (number %100) //10
    hundreds = number//100
 # Проверка дали числото се дели на всяка своя цифра
    
if number % hundreds == 0 and number % tens == 0:
    print(f'{hundreds}:{tens}:{units} и се дели на всяка своя цифра')

else:
    print(f'{hundreds}:{tens}:{units} и не се дели на всяка своя цифра')


          