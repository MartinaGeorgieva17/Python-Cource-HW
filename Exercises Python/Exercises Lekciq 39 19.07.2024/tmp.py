# 1..........................

# def foo(*args):
#     print(args)

# foo(1,2,3)
# foo(1,2)

# 2......................
# def bar(x,y):
#     print(f'x={y}')
#     print(f'y={y}')

# data = (1,2)
# # bar(data[0], data[1])
# bar(*data) #еквиваленто наразпекетирана форма -> # bar(data[0], data[1])


# 3...........................................

# def bar(x,y):
#     print(f'x={y}')
#     print(f'y={y}')

# new_data = {
#     'x':1,
#     'y':2
# }

# bar(y=3, x=1)
# bar(y=new_data['x'], x=new_data['x'])

# bar(**new_data)