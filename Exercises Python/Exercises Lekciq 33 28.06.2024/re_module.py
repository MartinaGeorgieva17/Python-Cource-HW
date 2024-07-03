# 1..REGEX OBJECT AND RE MODULE..........................................
# Object method

# import re

# test_string = '1234'

# #using regex object method: 
# rx = re.compile (r'^\d+$')
# m= rx.search(test_string)
# print(m)




# 2..Example 2: Re module:...................................................


# import re

# test_string = '1234'


# #using re module function
# m= re.search (r'^\d+$', 
#               test_string)
# print(m)




# 3.Regex search.(string[, start[, end]]))...............................................................


# import re

# test_string = '1234abc456'

# # using regex object method:
# rx = re.compile(r'abc')


# m = rx.search(test_string, 0, 6)

# print(m)

# m = re.search(r'abc', test_string[:7])
# print(m)



# 4.Match. Example................................

# import re

# test_string = '1234abc456'

# # using regex object method:
# rx = re.compile(r'abc')
# m = rx.match(test_string, 0, 6)

# print(m)


# 5.Match Example..............................................


# import re

# test_string = '1234abc456'


# # using regex object method:
# rx = re.compile(r'^\d')
# m = rx.match(test_string)


# #the same as
# rx = re.compile(r'^\d')
# m = rx.search(test_string)


# print(m)





# 6.FINDALL...............................................

# import re

# text = '1234abc456abcabc'
# rx = re.compile('\\dabc')

# res = rx.findall(text)
# print(res)




# 7.FINDALL......................................


# import re

# text = '1234abc456abcabc'
# rx = re.compile(r'dabc')

# res = rx.findall(text)
# print(res)





# 8.Sub (substitude) Example...................................................
# Task: remove all digits from string


# import re

# text = '1234abc456abcabc'
# rx = re.compile(r'\d')
# text_replaced =rx.sub('', text)

# print(text_replaced)




# 9.Match Object........................................................



# import re

# text = '1234abc456abcabc'
# rx = re.compile(r'abc')

# m = rx.search(text)
# print(m)



# 10. Match Object, Task: get digit sequence


# import re

# text = '1234abc456abcabc'
# rx = re.compile(r'(\d+)')

# m = rx.search(text)
# print(m.group())



# 11.Match Object............................

# import re

# text = '1234abc456abcabc'
# rx = re.compile(r'(\d+)(\w+)')

# m = rx.search(text)
# print(m.group(1))
# print(m.groups())


# 12.Match Object with 'Start' and 'end'..................................

# import re

# text = '1234abc456abcabc'
# rx = re.compile(r'(\d+)([a-z]+)')

# m = rx.search(text)
# print(m.group(1))
# print(m.group(2))
# print(m.groups())
# print(m.start())
# print(m.end())

