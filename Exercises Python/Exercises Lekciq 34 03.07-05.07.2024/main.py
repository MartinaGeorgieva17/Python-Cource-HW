# 1.Regex Examples..........................
# Beutify Task: 
# We must extract code from non-commented lines in a file and place line numbers infront

import re
import os 

print(os.getcwd())

def get_input_text(filepath):
    with open (filepath, 'r') as file:
        return file.read

def beautify_text(input_text): 
    pass


#get input file content
if __name__ == "__main__":
    input_text = get_input_text('./example.txt')
    print(input_text)


#     # beautyfied_text = beautify_text (input_text)
#     # write_to_file(beautyfied_text, filepath = "beautified.txt")




