#Дадени са няколко цели числа. Напишете програма, която намира онези
#подмножества от тях, които имат сума 0. Примери:
#- Ако са дадени числата {-2, -1, 1}, сумата на -1 и 1 е 0.
#- Ако са дадени числата {3, 1, -7}, няма подмножества със сума 0. 

def find_subsets(nums):
    # Създаване на две списъка с половината от числата
    half = len(nums) //2
    subset1 = nums[:half]
    subset2 = nums[half:]

# Създаване на всички възможни суми от подмножества от първата половина
    sums1 = {0}
    
    for num in subset1:
        sums1 |= {num + s for s in sums1}

    # Намиране на всички възможни суми от подмножества от втората половина
    sums2 = {0}
    for num in subset2:
        sums2 |= {num + s for s in sums2}

    # Намиране на подмножествата със сума 0
    subsets_with_sum_zero = [(s, 0 - s) for s in sums1 if -s in sums2]

    return subsets_with_sum_zero

# Дадени цели числа
nums = [-2, -1, 1]

# Намиране на подмножествата със сума 0 и извеждане на резултата
zero_sum_subsets = find_subsets(nums)
if zero_sum_subsets:
    print("Подмножества със сума 0:")
    for subset in zero_sum_subsets:
        print(subset)
else:
    print("Няма подмножества със сума 0.")
