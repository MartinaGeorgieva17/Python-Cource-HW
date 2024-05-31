# Помолете потребителя да въведе две точки (x и y координати) и да намери 
# разстоянието между тях.
# Вход: (3, 4), (6,5) Вход: (-3, -4), (4,5)
# Изход: 3.1622776601683795 Изход: 11.40175425099138

import math

def distance_between_points(x1,y1, x2, y2):
    distance = math.sqrt((x2 - x1)**2 +(y2-y1)**2)
    return distance 

def main():
    # Въвеждане на координатите на първата точка
    
    x1, y1 = map(float, input('Въведете данните за първа точка (x1, y1):').split(','))
    # Въвеждане на координатите на първата точка
    x2, y2 = map(float, input('Въведете данните за втора точка (x2, y2):'). split(','))

# Изчисляване на разстоянието между точките
    dist = distance_between_points(x1, y1, x2, y2)

 # Отпечатване на резултата
    print(f'Разстоянието между точките ({x1}), ({y1}) и ({x2}), ({y2}) е:', dist)

if __name__ == '__main__':
    main()
