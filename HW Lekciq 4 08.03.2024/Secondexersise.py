#Напишете програма, която показва знака (+ или -) от частното на две реални числа, 
#без да го пресмята. 

import math

numerator = 3
denominator = 6

sign = math.copysign(1, numerator/denominator)
sign_symbol = '+' if sign == 1 else "-"

print('Знакът на частното число е:', sign_symbol)


