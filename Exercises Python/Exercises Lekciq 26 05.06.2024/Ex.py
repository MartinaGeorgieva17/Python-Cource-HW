# 1...............................

# class A:
#     def __init__(self,x):
#         self.x = x

#     def foo(self):
#         print(self.x)

# a = A (5)
# a.foo()



# 2...................
# class A:
#     def __init__(self,x):
#         self.x = x

#     def foo(self):
#         print(f'Foo in A: {self.x}')

# class B(A):
#      def __init__(self, x):
#          super().__init__(x)

#      def foo(self):
#          print(f'Foo in B: {self.x}')

# b=B(5)
# b.foo()


# 3.......................
# class A:
#     def __init__(self,x):
#         self.x = x

#     def foo(self):
#         print(f'Foo in A: {self.x}')

# a1= A(1)
# a2=A(2)
# print(a1.x)
# print(a2.x)

# a1.foo()
# a2.foo()



# 4..........................

# def total(initial=5, **num):
#     print(initial)
#     print(num)
    
# total(100,a=1,b=2,c=3)



# 5.......................... ERROR......................
# def total(initial=5, **num):
#     print(initial)
#     print(num)
    
# total(100,1,2,3)


# 6......................................

# def total(initial=5, *args, **kw):
#     print(initial)
#     print(args)
#     print(kw)
    
# total(100,1,2,3, a=1)


# 7...........................................
def test_scores(total_questions=0, total_correct=0):
    return int(total_correct) / int(total_questions)

test_score = test_scores(0,20)
print(test_score)
