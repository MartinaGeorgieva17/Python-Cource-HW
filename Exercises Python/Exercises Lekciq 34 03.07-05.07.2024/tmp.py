# import re 


# input_str = """
# line1
#          # line 2
#     line3
# # line 4
#     line5
#     lne6
#    #
# line7
# """

# #Matching lines starting with '#', optionally with leading space 

# comment_lines_re = re.compile(r'^\s*#.*$', re.MULTILINE)
# whitespace_re = re.compile(r'\s+')

# # Намиране на всички съвпадения
# # matches = comment_lines_re.findall(input_str)

# # Принтиране на резултатите
# # for match in matches:
#     # print(f"Съвпадащ ред: '{match}'")

# #pattern.sub(repl, string, count=0, flags=0)

# replaced = comment_lines_re.sub("", input_str )
# print(replaced)

# replaced = whitespace_re.sub("\n", replaced)
# print(replaced)

