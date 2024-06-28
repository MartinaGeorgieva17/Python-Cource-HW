# 1.Anchors ...............................


# rx = re.compile(r'^abc$')
# test_strings= [
#     'abc',
#     'abc123',
#     '123abc'
# ]


# 2.Anchors.....................................
# import re

# rx = re.compile(r'^l.+2$')
# test_strings= [
#     '''line1
#     line2'''
# ]


# for test_string in test_strings:
#     m = rx.search(test_string)
#     if m:
#         print(f'{test_string}match!')
#     else:
#         print(f'{test_string}Does not match!')


# 3.Word Boundary.....................................
# ................................................
# \b => between \w and \W characters
# \d = [0-9]
# \D = [^0-9](any non-digit symbol)
# \w = [A-Za-z0-9]
# \W = [^a-zA-Z0-9_]


# 'a2' - no word boundry 
# 'a!' - word bpundary 

# import re

# rx = re.compile(r'\b')
# test_strings  = [
#     '', #no match 
#     'a',
#     'aa',
#     'a!a',
# ]


# for test_string in test_strings:
#     m = rx.search(test_string)
#     if m:
#         print(f'{test_string} Match!')
#     else:
#         print(f'{test_string} Does not match!')



# 4............................................................
# import re 

# strings = [
#     'ana',
#     'ana bel'
# ]

# rx = re.compile(r'^.+$')

# for strings in strings: 
#     res=rx.findall(strings)
#     print("{} maitches in {}".format(len(res), strings))


# 5................................................
# import re 

# test_strings = [
#     '', #
#     'a', #1
#     '@', #1
#     '@a', #
#     'aa', #2
#     'a!', #2
#     'a,a', #4
#     'a_a'  #2
# ]

# rx = re.compile (r'\b');

# for string in test_strings: 
#     res = rx.findall(string)
#     print(f'{len(res)} word boundars cointed in {string}')