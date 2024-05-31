#Да се напише програма, която да създава tuple (a, b), представящ броят на 
#уникалните елементи в дадено множество и b представящо броят на дублицираните 
#елементи в множеството. Множеството да се въвежда от клавиатурата.

def count_elements(set_input): 
    unique_elements = len(set_input)
    duplicated_elements = len(set_input) - len(set(set_input))
    return(unique_elements, duplicated_elements)

def main(): 
    # Въвеждане на множеството от клавиатурата
    set_input = set(input('Въведете елементите на множеството разделени със запетая:').split(','))
# Извикване на функцията за броене на уникалните и дублирани елементи   
    result = count_elements(set_input)
    
    # Извеждане на резултата
    print('Брой уникални елементи:', result[0])
    print('Брой дублирани елементи:',result[1])

if __name__ == '__main__':
    main()