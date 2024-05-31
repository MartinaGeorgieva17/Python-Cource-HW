#1.Множества...........
#set1 = {1,2,3,3,2}
#print(set1)


#2. Primer..........
#data = [1,2,3,3,2]
#unique_data = set(data)
#print(unique_data)


#3. Example............
#data = [1,2,3,3,2]
#unique_data = list(set(data))
#print(unique_data)


#4. Цикъл върху сет /loop on set........................

#for el in {1,2,3,3,2}:
#    print(el)


#5. Добавяне на елемент към множество/Add element .....................

#set1 = {1,2,3,3,2}
#set1.add(4)
#print(set1)


#6. Update  ..................................

#set1 = {1,2,3,3,2}
#set1.add(4)
#set1.update([1,2,5,6])
#print(set1)


#7. Remove element .............................
#set1 = {1,2,3,3,2}
#set1.remove(2)
#print(set1)

#8. Обединение на множества /Sets Union ................

#s1 = {1,2,3}
#s2 = {2,3,4}

#print(s1.|s2) 
#print(s1.union(s2))


#9 Сечение на две множества/ INTERSECTION..................
#s1 = {1,2,3}
#s2 = {2,3,4}
#print(s1.union(s2))
#print(s1.intersection(s2))


#10. Разлика на две множества/DIFFERENCE........................

#s1 = {1,2,3}
#s2 = {2,3,4}
#print(s1.difference(s2))
#print(s2.difference(s1))


#11. Сравняване на множества/Superset i subset ......................

#s1 = {1,2,3}
#s2 = {2,3,4}
#print(s1.union(s2))
#print(s1.difference(s2))
#print(s2.difference(s1))

#print (s1<s2)

#Отговор: Falsh


#12. Subset /Example (дали едното включва другото и обратното).................
#s1 = {1,2,3,4}
#s2 = {1,2,3,4,5}
#print(s1<s2)

#Отговор: True 



#12 Тупъли/примери...........................
#t= (1,2,3)
#t2= 1,2,3
#print(t)
#print(t2)



#12.1 ............................
#тупъл от един елемент/ако искаме тупъл с цифрата 1
#винаги когато имаме запетая е тупъл 

#t2 = (1) #this is not a tuple, but an ineger 
#print(type(t2))

#Rehsenie na primer 12.1
#t1 = (1, ) # this is a tuple 
#print(t1)



#12.3................

#x=1
#y=2

#x,y = 1,2  #ekvivalentno na x=1 i y=2, po-lesno e da go napishem na edin red 
#print(x)
#print(y))




#12.4 Tuple Operations.............

#birth_date = (22, 3, 1990)
#if we want change/change tuple/convert to list
#l = list(birth_date)
#l[2] = 1991
#birth_date = tuple(l)

#print (birth_date)



#12.5.......................

#t = tuple([1,2,3])
#print(t)


#12.6 Tuples...............

#user_input = input('Enter numbers:')
#print(user_input)


#12.7 Добавяне на информация в Tuple....................
#user_input = tuple(input('Enter a number:'))
#print(user_input)



#12.7 Tuples/Вградени функции в Tuple/compare tuples.................

#t1 = (1,2,3)
#t2 = (4, 5)

#if t1 < t2:
#    print("t1 е по-малък от t2")
#elif t1 > t2:
#    print("t1 е по-голям от t2")
#else:
#    print("t1 и t2 са равни")



#12.8 Frozenset Структура /не променяем сет.............................

#s = set ([1,2,3])
#fs = frozenset ([2,3])

#print(s>fs)

#В случая fs frozen set включчва цифрите на set и връща отговор true 










#Exersise lekciq 7 ......................................................
#1............................



#name = '123'
#r = range(3)
#l = [1,2,3]
#t = (1,2,3)


#print(name[0])
#print(r[0])
#print(l[0])
#print(t[0])

#print last element: 
#print(name[-1])
#print(r[-1])
#print(l[-1])
#print(t[-1])



#2 Concatenation /izkliychenie za range  ....................................

#print (name+name)
#print (l+l)
#print (t+t)



#3Достъпване до елемент и промяна /списък .................................

#t = ([1,2,3],)
#print(t[0])

#ako iskame da dostupim purvi element i promenqme na 9
#printira spisuk 
#t[0][0] = 9
#print(t)



#4 Range.......................

#range did not generated elements in advanced, only when needed
#Винаги има фиксирана памет/ без значение от range
#Генерира винаги до -1

#r1 = range(3)
#r2 = range (3000000)


#5 print list l1 .....................
#l1 = [1,2,3]
#print(l1*3)



#6. Slice / Range - връща винаги списък ................
#r1 = range(10)
#print(r1)
#print(list(r1[2::]))




#7.  Range from 2 to 10 / четни числа ...................................

#r1 = range(2, 11, 2)

#print(list(r1))




#8....................
#Range from 2 to 10 / slisvame четни числа ...................................


#r1 = range(2, 11, 2)

#print(list(r1))

#l1 = list(range(1,11))
#print(l1)
#l2 = l1[1::2]
#print(l2)



# 9. Reverse Списък.......................

#li = [1,2,3]
#l_reversed = li[-1::-1]

#print(l_reversed)




#10. Филтриране на списък /........................
#Създаваме нов списък от съществуващ с елементи умножени по 2
#Вариант 1/Грешен начин/Мапинг 

#l1 = [1,2,3,4]
#l2 = list ()
#for el  in l1:
#   l2.append (el**2)

#print(l2)



#Вариант 2 ...................
#По-лесен вариант 
#lIST Comprehensions => good 

#l2 = [el**2 for el in l1]
#print(l2)



#11. Maping ........................
#task: map symbols in string to its ascii code 

#print(ord('a')) # dava koda na bukvata /dopulnitelna informaci 
#variant 1
#string ='abc'
#codes[ord(el) for el in string]
#print(codes)


#variant 2.........
#l =[1,2,3,4,5]
#l2 = list()
#for el in l:
#    if el%==0:
#        l2.append(el)
#print(l2)

#compehations reshenie ...............
#l =[1,2,3,4,5]
#l2 = [el for el in l if el%2==0]
#print(l2)


#12.task: flatten list of list .......................

#m = [
#    [1,2,3],
#    [4,5,6],
#    [7,8,9]
#]

#flatten_m = [1,2,3....,8,9] # kraina cel na zadachata 

#flatten_m = [el for row in m for el in row]

#print(flatten_m)




#13. lIST COMPLIHAION ................
#TASK: CREATE list from dictionary 


#d= {'a':1, 'b':2, 'c':3}
#l = [key + str(value) for key, value in d.items()]
#print(d.items())

#print(l) ## ['a1', 'b2], 'c3']



#14...........Create Dictionary from string values 

#value = [1,2,3]
#string ='abc'

#d = {string[idx]:val for idx, val in enumerate(value)} 
#print(d)



