def great(user_name):
    print(user_name)

class A:
    def great(self, user_name):
        print(user_name)

class B(A):
    pass


#Call function 
great('Ada')

#creata instance of A
a1=A()
b1=A()

#Call method
a1.great('Ada Byron')
b1.great('Ada Byron')


#create instance of B 
b1= B()
