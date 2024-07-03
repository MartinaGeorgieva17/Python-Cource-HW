# 1.............................................



# import re

# rx = re.compile(r'c(a|o)t') #'cat' or "cot"
# rx = re.compile(r'ca|ot') # "ca" or "co"





# 2..Example.....................................
# Когато имаме кръгли скоби е приориетно и трябва да го има задължително


# import re 

# text = 'I love cats. He love dogs.'
# pattern = re.compile (r"(cat|dog)s")


# result = pattern.findall(text)
# print(result)




# 3...............................................

# import re 

# text = 'I love cats. He love dogs.'
# pattern = re.compile (r"(?:cat|dog)s")


# result = pattern.findall(text)
# print(result)





# 4.............................................

# import re 

# text =""" 
# Ivan Ivanov: 30 years old;
# Petar Petrov:25 years old;
# """


# # using capturing group to get names and ages 

# pattern = re.compile(r"(\w+)\s(\w+):\s?(\d+)\s")
# matches = pattern.findall(text)

# for match in matches:
#     print("First Name:", match [0])
#     print("Last Name:", match [1])
#     print("Age:", match [2])



# 5..Групиране/matches Regular Expressions........................................


# import re 

# text =""" 
# Ivan Ivanov: 30 years old;
# Petar Petrov:25 years old;
# """
# #using capturing group to get names and ages 
# pattern = re.compile(r"(\w+\s(\w+)):\s?(\d+)\s")
# matches = pattern.findall(text)

# for match in matches:
#     print("Group 1:", match [0])
#     print("Group 2:", match [1])




# 6.......................................................

# import re 

# text =""" 
# Ivan Ivanov: 30 years old;
# Petar Petrov:25 years old;
# """
# #using capturing group to get names and ages 
# pattern = re.compile(r"(?:\w+\s(\w+)):\s?\d+\s")
# matches = pattern.findall(text)

# for match in matches:
#     print("Group 1:", match [0])
#     print("Group 2:", match [1])



# 7..............................................................


# import re 

# text =""" 
# Ivan Ivanov: 30 years old;
# Petar Petrov:25 years old;
# """
# #using capturing group to get names and ages 
# pattern = re.compile(r"(?:\w+)\s\w+:\s?(\d+)\s")
# matches = pattern.findall(text)

# for match in matches:
#     print("Group 1:", match [0])
#     print("Group 2:", match [1])


# 8...........................................................

# import re 


# rx = re.compile(r'(?:straw|rasp)berries')

# test_strings = [
#     'straw berries',  # not
#     'I love strawberries',  # ok
#     'I love rasp berries', # not 
#     'I love raspberries', # ok 
#     'I love berries' # not
# ]

# for string in test_strings:
#     m = rx.search('string')
#     if m:
#         print(f'{string} # ok')
#     else:
#         print(f'{string} # Not')



# 9.............................

# import re

# strings =[
#     "a123a", #ok
#     "a123ab", #not
#     "caaac", #ok
#     "ff",  #ok
# ]

# rx = re.compile(r'^([a-z]).*\1$')

# for string in strings: 
#     m = rx.search(string)
#     if m:
#         print (f'{string} match')
#         print (f'{string} not match')


# 10............................................

# import re 

# text =""" 
# Ivan Ivanov: 30 years old;
# Petar Petrov:25 years old;
# """
# #using capturing group to get names and ages 
# pattern = re.compile(r"(?:P<firs>\w+\s(?<second>\w+)):\s?(?P<age>\d+\s")
# matches = pattern.findall(text)

# for match in matches:
#     print("First Name:", match ['first'])
#     print("Second Name", match ['second'])
#     print("Age:", match ['age'])



# 11.Example with Regular expression, search and check for matches 
# and printthe extracted information.....................................................


# import re 

# text = """ 
# Ivan Ivanov: 30 years old;
# Petar Petrov:25 years old;
# """
# #using capturing group to get names and ages 
# pattern = re.compile(r"(?P<first>\w+)\s(?P<second>\w+):\s?(?P<age>\d+)\s")
# m = pattern.search(text)

# if m:
#     print("First Name:", m.group('first'))
#     print("Second Name", m.group('second'))
#     print("Age:", m.group('age'))
# else:
#     print("No matche found")