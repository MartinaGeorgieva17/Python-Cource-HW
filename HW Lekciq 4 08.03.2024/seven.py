#Напишете програма, която прилага бонус точки към дадени точки в интервала [1..9] 
##чрез прилагане на следните правила:
#- Ако точките са между 1 и 3, програмата ги умножава по 10.
#- Ако точките са между 4 и 6, ги умножава по 100.
#- Ако точките са между 7 и 9, ги умножава по 1000.
#- Ако точките са 0 или повече от 9, се отпечатва съобщение за грешка. 

def apply_bonus(points): 
    if points >=1 and points <=3:
        return points *10

    elif points >=4 and points <=6:
        return points *100
    
    elif points >= 7 and points <=9:
        return points *1000

    else: 
        print('Грешка')

    return None 

# Примери на прилагане на бонус точки
points1 = 2
points2 = 5 
points3 = 8 
points4 = 12 

# Прилагане на бонус точки и извеждане на резултата
print("Точки:", points1, ", След прилагане на бонус:", apply_bonus(points1))
print("Точки:", points2, ", След прилагане на бонус:", apply_bonus(points2))
print("Точки:", points3, ", След прилагане на бонус:", apply_bonus(points3))
print("Точки:", points4, ", След прилагане на бонус:", apply_bonus(points4))