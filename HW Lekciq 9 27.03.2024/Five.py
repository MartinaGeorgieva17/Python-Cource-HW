# Задача 5. Помолете потребителя да въведе координатите на дадена точка и да намери 
# разстоянието на точката до началото (0, 0). За абсолютна стойност може да използвате
# вградената функция abs(). Формулата за намиране на разстояние 
# !(�! − �")" + (�! − �")" формула: корен квадратен (x1 - x2) на квадрат + (y1-y2) на квадрат 
# Вход: (3, 4) Вход: (-3, -4)
# Изход: 5 Изход: 5





def distance_origin(x,y):
     # Използваме формулата за разстояние между две точки
     distance = (x**2 + y**2)**0.5
     return distance

 # Въвеждане на координатите на точката от потребителя

def main():
     x = float(input('Въведете (x) на точката: '))
     y = float(input('Въведете (y) на точката: '))

  # Изчисляване на разстоянието до началото
     distance  = distance_origin(x,y)

    # Резултат
     print(f"Разстоянието на точката({x}), ({y})до началото на координатната система е: {distance}")

if __name__ == '__main__':
     main()

