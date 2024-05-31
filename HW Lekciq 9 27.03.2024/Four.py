# Да се напише програма, която създава речник, който да съдържа следните 
# операции |, &, -, между две множества a и b. Множествата да се въвеждат от 
# клавиатурата. Речникът да има за ключ конкретната операция, а за стойност полученият 
# резултат от изпълнението на операцията.

# Вход: a ={1,2} b = {2, 3}
# Изход:
# {
# "{1, 2} | {2, 3}": {1, 2, 3},
#  "{1, 2} & {2, 3}": {2},
#  "{1, 2} - {2, 3}": {1}
# } 


def create_dictionary(a,b):
# Инициализираме празен речник за съхранение на резултатите от операциите
    result = {}
# Изпълняваме операцията за обединение на множествата и я добавяме към речника
    result[f'{a} | {b}'] = a.union(b)
 # Изпълняваме операцията за сечение на множествата и я добавяме към речника    
    result[f'{a} & {b}'] = a.intersection(b)
# Изпълняваме операцията за разлика на множествата и я добавяме към речника
    result[f'{a} - {b}'] = a.difference(b)
    return result

def main():
# Въвеждане на елементите на множество a от потребителя
    a_input = input('Въведет стойностите на множеството а, разделени със запетая и без интервали :')
# Въвеждане на елементите на множество b от потребителя
    b_input = input('Въведет стойностите на множеството b, разделени със запетая и без интервали :')
    
# Преобразуване на въведените данни в множества
    a = set(map(int, a_input.split(',')))
    b = set(map(int, b_input.split(',')))
# Извикване на функцията за създаване на речник
    result_dictionary = create_dictionary(a, b)

# Извеждане на резултата
    print(result_dictionary)

if __name__ == '__main__':
   main()



 
    