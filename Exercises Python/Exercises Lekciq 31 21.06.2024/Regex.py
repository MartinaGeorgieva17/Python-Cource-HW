# Regex - Regular Expession 
# 1................................
# import re 
# # regex that matches sequences of 8 or more word characters (letters, numbers, underscores  )
# rg = =re.compiler(r'^w{8,}$')

# password = 'abc - 123456'

# m=rg.search(password)
# if m :
#     print(f'{password} is valid')
# else:
#     print (f'{password}is not valid')




# 2...................................
# \bcan\b - regular expression

# import re 

# re_str ='can\\tl'
# print (re_str)




# 3.Примери....................................................



# import re 

# re_str ='\\b'
# row_str = r'\b'
# print (re_str)
# print(row_str)



# 4....................................
# https://regex101.com/- проверка 


# import re 

# test_string ='\\stop'

# patterns = [
#     '\\stop',
#     '\\\stop',
#     r'\\stop'
# ]

# for pattern in patterns:
#     if re.match(pattern, test_string):
#         print(f'Pattern/{pattern}/MATCHED string {test_string}!')
#     else:
#         print(f'Pattern/{pattern}/DID NOT MATCHED string {test_string}!')




# 5..................................................................
# Regular and Meta Symbols 


# import re 

# txt = "Hello, welcome to my world."

# res = txt.find ("welcome")
# print(res)



# 6..................................

# Regular and Meta Symbols. Special Characters: ^ $ \ . * + ? ( ) [ ] { } | 


# import re 

# text = "try to match : 2+3"
# rx = re.compile(r'2\+3')

# res = rx.search(text)
# if res:
#     print(res.group())



# 7.Regular Expresson.............................................................
# Cheet-sheet : https://www.debuggex.com/cheatsheet/regex/python (табличка)



# import re 

# text = "cat"
# rx = re.compile(r'[cm]at')

# # /[cm]at => 'cat', 'mat' - така работи системата, първо преминава през 'c',
# # после през 'm', пак ще работи и ще има съвпадение, без значене от последователността 


# res = rx.search(text)
# if res:
#     print(res.group())




# 8.Regular Expresson............................................
# ASCII таблицата спомага за рзрешаване на задачи 
# import re 

# text = "2"
# rx = re.compile(r'[A-z]')


# res = rx.search(text)
# if res:
#     print('Match')

# else:
#     print('Do not Match')


# 9..........................................

# import re 

# text = "[]"
# rx = re.compile(r'[A-z]')


# res = rx.search(text)
# if res:
#     print('Match')

# else:
#     print('Do not Match')


# 10......................................
# ^ - има различни значчения спрямо нейното местоположение 
# [^abc] - всеки един символ без конкретните три abc


# import re 

# text = "7"
# rx = re.compile(r'[^abc]')


# res = rx.search(text)
# if res:
#     print('Match')

# else:
#     print('Do not Match')





# 11................................................
# ^ - има различни значчения спрямо нейното местоположение 
# [^abc] - всеки един символ без конкретните три abc



# Task: включва съгласните .................
# import re 

# matched = re.findall(r'[aeiouy]', 'astroid');
# print(matched)




# # Task: изключва съгласните .............................

# import re 

# matched = re.findall(r'[^aeiouy]', 'astroid');
# print(matched)




# 12................................................

# /[0-9][a-c]/ =>

# '2a'
# '23a'




# 13..........................................


# import re

# text = "The quick brown for jumps over the lazy dog "
# pattern = re.compile (r'\w+')
# result = pattern.findall(text)
# print(result)

# text = """line1
# line2
# line3 line4"""

# pattern = re.compile(r'line\d\s')
# result = pattern.findall(text)
# print(result)




# 14..............................................

# import re 
# text = ''
# pattern = re.compile(r'a')
# result = pattern.findall(text)
# print(result)



# 15......................................................

# import re 

# text = '1aaaa'
# pattern = re.compile(r'a*1')
# result = pattern.findall(text)
# print(result)



# 16............................................


# import re 

# text = '1aaaa1'
# pattern = re.compile(r'1a*1')
# result = pattern.findall(text)
# print(result)




# 17....................................

# import re 

# text = '11'
# pattern = re.compile(r'a*1')
# result = pattern.findall(text)
# print(result)




# 18............................................

# import re 


# test_strings=[
#     'aa',  #not
#     '1aa',  #not
#     '11',  #ok
#     '1aaaa1'  #ok
# ]
# pattern = re.compile(r'1a*1')
# for test_str in test_strings:
#     result = pattern.findall(test_str) 
#     print(f'{test_str}:{result}')





# 19.................................................
# symbol   ? (или) след символ (нула или един път)

# import re 


# test_strings=[
#     'aa',  #not
#     '1aa',  #not
#     '11',  #ok
#     '1aaaa1'  #ok
# ]

# pattern = re.compile(r'1a?1')
# for test_str in test_strings:
#     result = pattern.findall(test_str) 
#     print(f'{test_str}:{result}')





# 20...........................................

# когато има * трябва да го има и символът след нея, пример: 'ab*c'

# \w{2,} - минимум два символа (това означава)

# a{ ,5}


# import re 

# # Match 1 followed by 3-5 'a', followed by 1
# test_strings=[
#     '1aa1',  #not
#     '1aaa1',  #ok
#     '11aaa1',  #ok
#     '1aaaaa1'  #not
# ]

# pattern = re.compile(r'1a{3,5}1')
# for test_str in test_strings:
#     result = pattern.findall(test_str) 
#     print(f'{test_str}:{result}')



# 21...................................................



# import re 

# # Match 1 followed by 3-5 'a', followed by 1
# test_strings=[
#     '1aa1',  #ok
#     '1aaa1',  #ok
#     '11aaa1',  #ok
#     '1aaaaa1'  #not
# ]


# pattern = re.compile(r'1a{,5}1')
# for test_str in test_strings:
#     result = pattern.findall(test_str) 
#     print(f'{test_str}:{result}')


# 22..............................................
# GREEDY QUANTIFIERS /a{2,5} => 'aaaaa' - започва търсенето от 5-ата и 
# после преминава към 4 а-та и така 



# import re 

# # Match 1 followed by 3-5 'a', followed by 1
# test_strings=[
#     'ala bala'
# ]


# pattern = re.compile(r'a.*a')
# for test_str in test_strings:
#     result = pattern.findall(test_str) 
#     print(f'{test_str}:{result}')





# 23...............................................................
# Когато искаме да не е GREEDY QUANTIFIER изполваме ?

# import re 

# # Match 1 followed by 3-5 'a', followed by 1
# test_strings=[
#     'ala bala'
# ]


# pattern = re.compile(r'a.*?a')
# for test_str in test_strings:
#     result = pattern.findall(test_str) 
#     print(f'{test_str}:{result}')




# 24.........................................................
# Когато искаме да не е GREEDY QUANTIFIER изполваме ? (въпросително след quantifier)


# import re 

# # Match 1 followed by 3-5 'a', followed by 1
# test_strings=[
#     'ala bala'
# ]


# pattern = re.compile(r'a.+?a')
# for test_str in test_strings:
#     result = pattern.findall(test_str) 
#     print(f'{test_str}:{result}')





# 25.........................................................

