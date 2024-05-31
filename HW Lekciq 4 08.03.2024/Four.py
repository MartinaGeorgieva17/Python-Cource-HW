# Напишете програма, която за дадена цифра (0-9), зададена като вход, извежда името
# на цифрата на български език.

 # Въвеждане на цифра от потребителя
digit = int(input('Изберете цифра от (0 до 9): '))

# Извеждане на името на цифрата на български език
if digit == 0:
    print ('Нула')

elif digit == 1:
    print ('Едно')

elif digit == 2:
    print ('Две')

elif digit == 3:
    print('Три')

elif digit == 4:
    print('Четири')

elif digit == 5:
    print('Пет')

elif digit == 6:
    print('Шест')

elif digit == 7: 
    print('Седем')

elif digit == 8:
    print('Осем')

elif digit == 9: 
    print('Девет')

else:
    print('Грешна цифра!')