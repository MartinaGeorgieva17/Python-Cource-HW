
# 1.....................................


# # numpy.ndarray(shape, dtype=float, buffer=None, offset=0, strides=None, order=None)[source]

# # Create one dimension array: TASK

# import numpy as np

# arr1d = np.array([1,2,3])
# arr2d = np.array([[1,2,3], [4,5,6]])

# print(f'arr1d: \n{arr1d}\n')
# print(f'arr2d: \n{arr2d}\n')

# print(f'arr1d.shape: {arr1d.shape}')
# print(f'arr2d.shape: {arr2d.shape}')



# 2................................
# Като списък:
# import numpy as np


# l=[1,2,3,4]
# a = np.array(l)

# print(l)
# print(a)




# 3....................



# import numpy as np 

# # set a constant Size for the length of the sequences.set

# SIZE = 5 

# # Caculate point to point sum on two lists

# def calculate_pytho_lists_p2p_sum():
#     # create 2 python's list
#     l1= list(range(SIZE)) #[0,1,2,3,4,]
#     l2 = list(range(SIZE)) #[0,1,2,3,4,]

#     print(list(zip(l1, l2)))

#     p2p_sum = [x + y for x, y in list(zip(l1, l2))] 
#     print(f'p2p_sum: {p2p_sum}')

# calculate_pytho_lists_p2p_sum()





# 3.2.................................
# Слайсване припомняне

# l = [1,2,3,4,5]
# print(l[0:2])



# 3.2........................
# Слепя ги 



# l1 =[1,2,3]
# l2=[2,3,4]

# print(l1+l2)






# 4............................

# import numpy as np 

# # set a constant Size for the length of the sequences.set

# SIZE = 5 

# # Caculate point to point sum on two lists

# def calculate_pytho_lists_p2p_sum():
#     # create 2 python's list
#     l1= list(range(SIZE)) #[0,1,2,3,4,]
#     l2 = list(range(SIZE)) #[0,1,2,3,4,]

#     result = a1+a2


#     # result = [(x+y for x,y in zip (l1, l2))]
#     print(result [0:5])

# # Timing execution:
# print ('Timing Lists Sum:')
# %time calculate_python_lists_p2p_sum()
# print('-'*50)
# print('Timing Arrays Sum:')
# %time calculate_numpy_arrays_p2p_sum()



# 5...........................
# Да напраивм масив от пайтън списък 

# import numpy as np 

# l =[1,2,3]
# a = np.array(l)





