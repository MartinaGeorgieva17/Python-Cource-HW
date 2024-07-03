# 1................................


# import re

# rx = re.compile(r'a.+?a')
# test_strings = [
#     'ala bala',
# ]

# for string in test_strings:
#     res = rx.search(string)
#     print(res)




# 2.............................................
# import re

# rx = re.compile(r'a.+?a')
# test_strings = [
#     'ala bala',
# ]

# for string in test_strings:
#     res = rx.findall(string)
#     print(res)




# 3.with MULTILINE................................................
# import re

# rx = re.compile(r'^Line\s*\d', re.MULTILINE)
# test_strings = [
#     '''Line 1
# # Line 2
# Line 3''',
# ]

# for string in test_strings:
#     res = rx.findall(string)
#     print(res)




# 4..with multiline and ignorecase..................................

# import re

# rx = re.compile(r'^line\s*\d', re.MULTILINE|re.IGNORECASE)
# test_strings = [
#     '''Line 1
# # Line 2
# Line 3''',
# ]

# for string in test_strings:
#     res = rx.findall(string)
#     print(res)



# 5..MAtcing passwords example........................................


# import re


# rx = re.compile (r'''^^
#                  (?=.*\d) #matcha digit anywhere in string
#                  (?=.*[A-Z]) # matcha A-Z anywhere in string 
#                  (?=.*[a-z])  ## matcha a-z anywhere in string 
#                  (?=.*[^\w\d\s:])
#                  ([^\s]){8,16}
#                  $
#                  ''', re.X)

# test_strings = [
#     '_}24I:9t58Tu?m@e',
#     '|YlzEc|1',
#     '#m_4xF%t"Bu5jeb$'
# ]


# for string in test_strings:
#     m = rx.search(string)
#     if m:
#         print(f'{string}=> VALID Password')
#     else:
#         print(f'{string}=> NOT valid Password')



# 6.......................................................

