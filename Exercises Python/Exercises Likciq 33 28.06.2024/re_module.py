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




# 3.................................................................


import re

test_string = '1234'

#using regex object method: 
rx = re.compile (r'^\d+$')
m= re.search (r'^\d+$', test_string)
print(m)