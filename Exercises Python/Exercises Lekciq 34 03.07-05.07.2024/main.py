# 1.Regex Examples..........................
# Beutify Task: 
# We must extract code from non-commented lines in a file and place line numbers infront

# import re


# def get_input_text(filepath):
#     with open (filepath, 'r') as f:
#         return f.read()
    

# def write_to_file(input_text, filename):
#     with open(filename, 'w') as f:
#         f.write(input_text)



# def beautify_text(input_text): 
#     comment_lines_re = re.compile(r'^\s*#.*$', re.MULTILINE)
#     whitespace_re = re.compile(r'\s+')

#     replaced = comment_lines_re.sub ('', input_text)
#     replaced = whitespace_re.sub ('n', replaced)
#     # print(replaced)
#     return replaced


# #get input file content
# if __name__ == "__main__":
#     input_text = get_input_text('./example.txt')
#     beautified = beautify_text (input_text)
#     write_to_file(beautified, filename = "beautified.txt")


# #     # beautyfied_text = beautify_text (input_text)
# #     # write_to_file(beautyfied_text, filepath = "beautified.txt")



# 2............................................
# Task: да зпишем името и телефона само на хората, които са с телефонни номера в Бг
# Extract name and [hone number for bg code (+359)


# import re

# input_text = """
# ivan: +359 88 123456
# maria: +42 123456
# john: 76438787438
# anna:+359 9883249
# dummy:+359 9kkkkkk49
# """

# # Регулярен израз за съвпадение на име и български телефонен номер
# name_tel_re = re.compile(r'^(\w+):\s*(\+359[\s\d]+)$', re.MULTILINE)

# # Намиране на всички съвпадения
# matches = name_tel_re.findall(input_text)

# # Изпишете всички съвпадения
# for name, tel in matches:
#     print(f"Име: {name}, Телефон: {tel}")




