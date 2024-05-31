# 1.NUMPY........................
# ..........................................


# import numpy as np 

# a = np.arange(1,10)
# l=list(range(1,10))

# print(a)
# print(l)

# Indexing (1D Array)

# print(l[3])
# print(a[3])
# print(a[-2])


# Slicing - едномерни масиви/1D ARRAY..............................
# print(a[2:6:2])
# print(a[5:])
# print(a[::-1])
# print(l[::-1])






# 2.Двумерни масиви/2D Array.........................

# ml=[
#     [1,2,3],
#     [4,5,6]
# ]

# ma=np.array( ml)

# print(ml)
# print(ma)

# print(ma[1,1]) #best practice!!!!!!!
# print(ma[1][1]) #not memory efficient!!!!!






# 3..................
# Exersise ...................



# ml=[
#     [1,2,3],
#     [4,5,6]
# ]

# ma=np.array( ml)

# print(ma)

# print(ma[-1,1])





# 4..............................
# Exersise - - с по-голям масив ......................


# m = np.arange(1,10).reshape(3,3)
# print(m)


# print(m[-1, -2]) #8

# print(m[1:, -2::])
# print(m[1:, -2::-1])






# 5......................................
# Exersise..................................

# m = np.arange(1,17).reshape(4,4)
# print(m)

# print(m[1::2, 1])






# 6..................
# Exersise................


# m = np.arange(1,17).reshape(4,4)
# print(m)

# print(m[-2:, 3])





# 7......................
# Exersise.............................

# m = np.arange(1,17).reshape(4,4)
# print(m)


# print (m[-2::-1, ::-2])





# 8........................
# Advanced Indexing


# a1 = np.arange(1,6)
# a2 = a1**2

# print(a1)
# print(a2)


# 9.................
# Advanced Indexing


# a1 = np.arange(1,6)

# print(a1)

# #Boolean Indexing

# print(a1>3)

#Отговор: FALSE, FALSE, FALSE, TRUE, TRUE



# 10.................
# Advanced Indexing................
# Можем по този начин от един масив да вземем само четни елементи
# import numpy as np 
# a1 = np.arange(1,6)

# print(a1)

# print(a1[[False, False, True, True, False]])




# 11.................
# Advanced Indexing................
# import numpy as np 
# a1 = np.arange(1,11)
# print(a1)
# mask = a1%2==0 
# print(mask)
# evens = a1[mask]





# 12.................
# Advanced Indexing/Едномерен масив ................
# import numpy as np 

# a2d = np.arange(1,5).reshape(2,2)
# print(a2d)

# print(a2d[[True, False]])





# 13.................
# Advanced Indexing/Хвърляне на грешка................
# import numpy as np 
# a1= np.arange(1,5)
# print(a1[[True]])





# 14.................
# Advanced Indexing/Двумерен масив
# import numpy as np 

# a1 = np.arange(1,5)
# a2d = np.arange(1,5).reshape(2,2)
# print(a2d)

# print(a2d[
#     [
#         [True, False],
#         [True, False]
#     ]
# ])




# 15.................
# Advanced Indexing.....................
# import numpy as np 
# a1 = np.arange(1,5)
# a2d = np.arange(1,10).reshape(3,3)
# print(a2d)


# mask = a2d%2==0
# print(mask)    #a2d_evens = a2d[mask]




# 16.................
# Advanced Indexing.....................
# import numpy as np 

# a1 = np.arange(1,5)
# a2d = np.arange(1,10).reshape(3,3)
# print(a2d)


# mask = a2d%2==0
# print(mask)  


# a2d_evens = a2d[mask]
# print(a2d_evens)




# 17..................................
# Integer Array Indexing/ Едномерен масив
# import numpy as np 


# a1 = np.arange(1,10)

# print(a1)
# print(a1[[0,1,0,1,8]])



# 18..................................
# Integer Array Indexing..................
# Task:Define the scores array 
# import numpy as np 

# scores = np.array([
#     [4,1],
#     [2,0],
#     [3,0],
#     [5,1],
#     [6,1]
# ])

# #Define the categories: Task
# categories = ['bad', 'good']


# good_mask = scores[:, 1]==1


# print(scores[:, 1]==0)
# bad_scores = scores [scores[:, 1]==0,0]
# print(bad_scores)

# # good_scores = [4,5,6]
# # bad_scores = [2,3]




# 19..................................
# import numpy as np 
# lets have a numpy array of repeated values 0,1 or 2

# indexes = np.array([0,2,1,2,0,1,2])

# # and an array of colors:
# colors = np.array(['red', 'green', 'blue'])
# print(colors[[0,0,0]])

# colors_map = colors[indexes]
# print(colors_map)



# 20. Numpy Reshaping and Resizing .................................
# import numpy as np 

# # Създаване на оригиналния масив (2x3)
# arr = np.array([[1, 2, 3], [4, 5, 6]])
# print('Original array (2x3):\n', arr)

# # Променяне на формата на масива на (3x2)
# arr3x2 = arr.reshape(3, 2)
# print('Reshaped array (3x2):\n', arr3x2)





# 21. Numpy Reshaping and Resizing .................................
# import numpy as np 

# # # Създаване на оригиналния масив (2x3)
# arr = np.array([[1, 2, 3], [4, 5, 6]])
# print('Original array (2x3):\n', arr)

# # Променяне на формата на масива на (3x2)
# arr3x2 = arr.reshape(3, 2)
# print('Reshaped array (3x2):\n', arr3x2)

# arr = np.array([[1, 2, 3], [4, 5, 6]])
# print('Original array (2x3):\n', arr)


# arr = np.arange(1,13)
# print(arr.reshape((2,3,2)))
# print(np.reshape(arr, (2,3,2)))


# arr2x2 = np.arange(1,9)
# print(arr)
# arr.resize(3,4)
# print(arr)
