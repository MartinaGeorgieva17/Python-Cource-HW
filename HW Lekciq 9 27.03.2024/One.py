#Да се напише програма, която сортира в нарастващ ред списък, чиито елементи 
#са tuples. При сортирането да се взема предвид последният елемент във всеки tuple. В 
#списъкът не трябва да се съдържат празни tuples.
#Вход: [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
#Изход: [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]

def sort_lists(lst): 
    lst = [sublist for sublist in lst if sublist] # Променено sublists на sublist
    sorted_list=sorted(lst, key=lambda sublist:sublist[-1])
    return sorted_list

my_tuples = [[2, 5], [1, 2], [4, 4], [2, 3], [2, 1]]
output_list = sort_lists(my_tuples)
print(output_list)