# Get Surrent directory/Get Cwd: 




# 1........................
# import os
# cwd = os.getcwd()
# print("Current Working Directory:", cwd)





# 2........................................

# import os

# cwd = os.getcwd()
# print("Current working directory:", cwd)

# with open(r'C:/Users/Martina/Desktop/Python2024/Python Cource HW/Home Works/Exersise Python/Exersise Lekciq 18 26.04.2024/Os_module.py') as f:
#     content = f.read()

# print(content)



# 3.Можем да накараме програмата да работи беззначение от папката, която сме използвали
# Промяната става по следния начин: .......................................
# Лоша практика !!!.............................

# import os
# cwd = os.getcwd()
# print("Current working directory:", cwd)

# new_cd = os.chdir('Попълваме желания от нас път')

# with open(r'C:/Users/Martina/Desktop/Python2024/Python Cource HW/Home Works/Exersise Python/Exersise Lekciq 18 26.04.2024/Os_module.py') as f:
#     content = f.read()

# print(content)




# 4. Get path of current file.......................................

# Така взимаме самия път до папката: 
# import os
# cwd = os.getcwd()
# print(__file__)


# Тест BASENAME - връща само името 
# Dirname - връща пълния път до файла 

# import os
# cwd = os.getcwd()
# print(__file__)

# print(f'Script Directory:{os.path.basename(__file__)}')
# print(f'Script Directory:{os.path.dirname(__file__)}')



# 5. List Dir /Example - Съдържание на една папка...........................

# import os
# cwd = os.getcwd()
# print('Crrent working Directory:', cwd)
# contents = os.listdir()
# print(contents)



# 6. Принтиране само на файлове ......................................
# import os
# cwd = os.getcwd()
# print('Crrent working Directory:', cwd)
# contents = os.listdir()
# for entry in contents:
#     if os.path.isfile(entry):
#         print



# 7. Ако искаме да ни покаже папка, да я отвори и да покаже нейното съдържание 
# os.walk.........................



# 8....................................
# Създаване на папки os.mkdir()
# Create directory...................

# mаkеdirs -Създава папка в папката

# os.mkdir('Data') #Създава папка Data

# os.mаkеdirs('Data/Audio') #Създава папка в папката




# 9....................................
# os.rmdir() - delete directory
# Не може да се изтрие цялото, изтрива само Audio 

# os.rmdir('Въвеждаме папката, която искаме да се изтрие: пример Data/Audio') # трие само папка Audio 



# 10............... 
# Изтрива цялаа папка - изтрива цялата Data 

# os.rmdir('Въвеждаме папката, която искаме да се изтрие: пример: Data/Audio')
# import shutil 
# shutil.rmtree('Въвеждаме папката, която искаме да се изтрие')




# 11................ 
# os.path module
# Get os name 

# import os
# print(os.name)


# cwd = os.getcwd()
# print('Current working directory', cwd)




# 11.  ............... 
# os.path module
# Създава папка в папката 


# 1.1.................................
# script_folder=os.path.dirname(__file__)
# print(f'script_dir:{script_folder}')

# audio_folder_path = 'Audio\mp3'


# 1.2.................................

# path1 = 'c:\\parent\file.ext'
# print(os.path.dirname(path1))



# 1.3.................................
# Без значение от операционната система - работи 
# Пример за join 

# import os

# path1 = 'parent'
# path2 = 'test.txt'
# print(os.path.join(path1,path2))



# 12.....................................................
# environ - стойността на променливата path 


# import os 
# print(os.environ['path'])
# print(os.environ.keys())




# 13.....................................................
# Python програма, която да създава друга програма, работи на Линукс
# echo



# 14.....................................................
# sys.version


# Извиква системата на python (с коя работим като версия)
# import sys
# print(sys.version)




# 15.....................................................
# Дава пътя, където е инсталиран Python 

# import sys 
# print(sys.version)
# print(sys.executable)



# 16.....................................................
# Импортване на модули /import lib 




# Изписва навсякъде, където намира lib 
# import sys
# for path in sys.path: 
#     print(path)


# Показва големината 
# print(sys.getsizeof(1))


# Показва как е финиширала програмата 
# Прекратява програмата 
# 0 - дава положителен изход, че всичко е било наред 

# sys.exit(0)




# 17. Echo.....................................................
# Правим прогамата да работи като echo, 
# да го направим като един стринг 

# import sys
# print(''.join(sys.argv[1:]))





# 18. .....................................................
# argpars - функиця, която позволява внедряване на много опции
#




# 19. Working with files.....................................................


