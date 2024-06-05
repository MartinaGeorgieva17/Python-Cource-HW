# 1...............................

# class A:
#     def __init__(self,x):
#         self.x = x

#     def foo(self):
#         print(self.x)

# a = A (5)
# a.foo()



# 2...................
# class A:
#     def __init__(self,x):
#         self.x = x

#     def foo(self):
#         print(f'Foo in A: {self.x}')

# class B(A):
#      def __init__(self, x):
#          super().__init__(x)

#      def foo(self):
#          print(f'Foo in B: {self.x}')

# b=B(5)
# b.foo()


# 3.......................
# class A:
#     def __init__(self,x):
#         self.x = x

#     def foo(self):
#         print(f'Foo in A: {self.x}')

# a1= A(1)
# a2=A(2)
# print(a1.x)
# print(a2.x)

# a1.foo()
# a2.foo()



# 4..........................

# def total(initial=5, **num):
#     print(initial)
#     print(num)
    
# total(100,a=1,b=2,c=3)



# 5.......................... ERROR......................
# def total(initial=5, **num):
#     print(initial)
#     print(num)
    
# total(100,1,2,3)


# 6......................................

# def total(initial=5, *args, **kw):
#     print(initial)
#     print(args)
#     print(kw)
    
# total(100,1,2,3, a=1)


# 7...........................................
# def test_scores(total_questions=0, total_correct=0):
#     return int(total_correct) / int(total_questions)

# test_score = test_scores(0,20)
# print(test_score)







# 8......................проект.....................

# 1.при създаване на проект, първо създаваме папка Src с файл main.py, 
# 2. После папка tests
# 3. В главната папка README.md
# 4. Папка docs - за условието на задачата 
# 5. python - m venv .myenv - създаване на виртуална среда за проекта, последното е име на файла
# 6. pip list - проверка на модули
# # 7. .myenv/Scripts/activate - първоо е името на файла 
# 8. pip install packages_name    - примерно pip install pandas
# 9. pip freeze > requirements.txt     - второто е името на файла, файлът дава информация за версиите
# 10. git init   - прави се само веднъж
# 11. .gitignore 
# слагаме я в главната папка на проекта (__pycache__/, .venv, env/, venv/,  i tn)
# ggs  - команда за Гит статус
# 12. git add -A
# 13. git add . - добавя всичко е текущата папка за comit
# 14. git comit - m ''Initial comit''
# 15. git push  качваме го в Гит Хъб 
# 16. README.md - файл с обща информация, какво прави кодът (инсталация, депендъсита, създадена ли е среда, features, introduction, installation)
# - как изглежда кодът или какво трябва да бъде направено екстеншън markdown с preview трябва да е 
# 17. И започваме с кода, това е

# Организация на код:

# 1.
