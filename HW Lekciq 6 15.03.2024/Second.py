#Да се състави програма, която ще изчисли сумата на 5, въведени от
#клавиатурата, естествени числа от интервала [10 ..5555].
#Вход: 1,2,3,4,5
#Изход: 15
      

def main():
    numbers = [int(input(f'Въведете число {i+1} от интервала [10, 5555]:')) for i in range(5)]
    numbers = [num for num in numbers if 10<= num <=5555]
    total = sum(numbers) 
    print('Сумата на въведените числа е:', total) 

if __name__ == '__main__':
    main()      


