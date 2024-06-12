# Когато искаме да работим заедно с друг човек по проект в GitHub,
#  даваме функция Fork, Create;

# Repo - запаметява всеки едно commit;

# Branch - основният main, подходящо е когато тестваме нов код да го сложим в нов branch
# защото по този начин не променяме основния код в main
# ако искаме да променим написаното от новя бранч към main, 
# използваме merge (правим го от main branch );


# Rebase  - добавя също прoмените в main, но премахва разделението, което се вижда в log graph

# При даден достъп в Github, ако искаме да ги обединим, цъкаме Pull Request и отиваме в края на страницата 
# и цъкаме Merge Request



# Pull - прави се когао искаме промените от Gihub да се пренесат към Visual Studio Code
# 1. Отваряме Visual Studio Code
# 2. New Terminal
# 3. git status (за проверка)
# 4. git log (можем да видим последните commit)
# 4. git pull





# ..............................................................................................




# 1. Нишково програмиране /Parallel Programming
# Task: sum of numbers 1..10_000_000
# Example............................................

import time

START = 1
END = 10_000_000



def sum_of_numbers(start,end):
    total = 0
    for num in range(start, end+1):
        total+=num
    
    return total


start = time.time()

# Run on Core1:
total_sum = 0

res1 = sum_of_numbers(START, round(END/2) )

# Run on Core2:

res2 = sum_of_numbers(round(END/2), END )

total_sum = res1+res2

print(f'Sum of{START}..{END} is {total_sum}')
end=time.time()
print(f'time:{end-start}')