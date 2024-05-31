#Итераторът, трябва да има вградена функция next
#Знае как да генерира всеки един елемент  

#1. Examples ................................

#l = [1,2,3]
#for el in l:
#    print(el)

# get l iterator............

#l_iter = iter(l)
#el1 = next(l_iter)
#el2 = next(l_iter)
#el3 = next(l_iter)
#print(el1, el2, el3)



#2 В range - итератор ...............

#r = range(3)
#r_iter = r.__iter__()
#print(next(r_iter))



#3. .................

#from itertools import count 

#for el in count(3, 9):
#    print(el)



#4. Да направим наш итератор
# Create custom iterable ......................

#class FiveNumbers:
#    def __init__(self) -> None: 
#        self.num = 1
#        self.count = 5
#
#    def __iter__(self):
#        return self
#    
#    def __next__(self):
#        while self.count>0:
#            self.count-=1
#            return self.num
#        raise StopIteration


#fn = FiveNumbers()
#for el in fn:
#    print(el)


#5. Генератори
