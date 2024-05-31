#1.0 Task: Ask user to enter 3 student names and their math scores
# Students: ivan, ocenka 5, stoqn s ocenka 3, petar s ocenka 6

#for i in range(3):
 ##   student = 'ivan'


#print(student)



#2.0 Какво са списъците ...............
#student1 = 'Ivan'
#student2 = 'Stoyan'
#student3 = 'Petar'

#index = student (v nashata zadacha), ivan = 0, stoyan = 1, petar = 2 /info
#students = ['Ivan', 'Stoyan', 'Petar']



#RAM: tova pravi ram pametta pri konkretnata zadacha/ info
#   students:0x421 () /info
 #  student1:0x123('ivan') /info
 #  student2:0x123('stoyan') /info
 #  student3:0x531('petar') /info


#2.1 Задача за списъци: ............

#l = [1,2,3]
#print(l)
#print(l[0])


#2.2................

#l = ['Ivan', 3]
#print('{} has {}'.format(l[0],l[1]))



#2.3............
#l = ['Ivan', 3]
#print(f'{l[0]} has {l[1]}')




#2.4 Списъци, задачи /da izleze Ivan has 3....................
#l = ['Ivan', 3]
#l[0] = 'Ivan' / variant edno 
#print(l[0].title()) 
#l[0] = l[0].title()

#print(f'{l[0]} has {l[1]}')

#print(l[0])




#2.5 Mutable vs immutable ....................
#Стрингът е Immutable #

#x = 'abc' #immutable/info
#l =['a', 'b', 'c'] #mutable/info


#l[0] = 'b'
#print(x[0])
#print(l[0])


#2.6 .............................

#name = 'Ivan'
#print(name.title())


#2.7 Списъци /Izpisva Ivan i ocenka 3...............
#l = ['ivan', 3]
#l[0] = l[0].title()
#print(f'{l[0]} has {l[1]}')



#2.8  Списъци/Задача: Вдигаме оценката нa Иван на 4..............

#l = ['ivan', 3]
#l[0] = l[0].title()
#l[1] = l[1]+1

#print(f'{l[0]} has {l[1]}')



#2.9 Индексиране / expression (rezltat)...............

#l = [1,2]
#x = 9
#print(2+2)
#print(l[0])
#print(x)


#2.10 Индексиране/indexing /list integer ..............
#l = [1,2,3]
#print(l[1+1])
#print(l[2])




#3.0 Списъци в списъци .............

#l = [1,[2,3], 4] #"purvi element edno, vtori e v skobite i tretiqt e 4"info
#rint(len(l))

#ako iskame da vidim samo troikata, pishem v zadachata 
#print(l[1][1])

# info/mojem da dadem i slednoto rehenie: x - l[1] i posle print(x[1])




#3.2 Списъци в списъци /indexirane .............
#l=[1,2,3], [4,5,6], [7,8,9]

#print(l)

#zadacha/kak da printirame samo 7 

#print(l[2][0]) #info 2 e kletkata, broim ot 0 suotvetno popademe v 7,8,9 
#info 0 otgoжarq na sedem, broeneto zapochva ot 0 



#3.3.4...... Обратно индексиране /започваме в обратна посока да броим с минус 1
#l = [1,2,3]
#print(l[0])
#print(l[-1])
#print(l[-4])





#3.3 Пример ID function .........

#x = 1
#l=[1]

#print(id(x))
#print(id(l))



#3.4 id function .............

#x = 1
#y = 1

#print(id(x))
#print(id(y))

#x = 2
#print(id(x))
#print(x,y)



#3.5 Списък - променяме данни и копие ...................

#x = [1]
#y = x
#x[0] = 9
#print(x)
#print(y)



#3.6...................
#x = [1]
#y = x
#print(id(x)) #1974360560832
#print(id(y)) #1974360560832
#x[0] = 9


#4. Копиране на списък - слайсване ..........

#data = ['ivan', 3]

#copy = data[:]
#data[1] = 6 

#print(data)
#print(copy)



#4.1 len function  ...........

#print(len('abc'))
#print(len([1,2,3,4,]))
#print(len(range(3)))



#4.3 Слайсване ...........отделяме/изрязваме първите два елемента 

#l[start:end:step]/info


#l = [1,2,3,4,5]
#print(l[0:2])

#4.4 slicing .............
#l[start:end:step] /info
#l[start:end], step => 1 
#l[start:],    end =>-1, step =>1
#l[:end],      start =>0 , step =>1
#l[:]          start =>0, end=>-1, step=>1


#l =[1,2,3,4,5]
#print(l[0:2]) #otgovor [1,2]
#print(l[0:2:1]) #otgovor[1,2]
#print(l[0:2:2]) #otgovor[1]


#4.5 Slicing - минусови цифри / в обратен ред ...........
#l =[1,2,3,4,5]

#print(l[0:-1])
#print(l[::-1]) #reversed 

#print[l:] #copy


#4.6 get the last 2 elements .....................
#l =[1,2,3,4,5]
#l1 = l[-2:]
#print(l1)



#4.7 append/Добавяне на елементи/списъци.....
#append - добавя винаги в края 


#l = [1,2,3]
#l2 = l.append(9)
#print(l)
#print(l2)


#5 insert добавя на конкретен индекс и какво ........

#l =[1,2,3]
#l.append(9)

#print(l)
#l.insert(0,9)

#print(l)


#info/ l.insert(0,9) # на коя позиция да сложим 0, избираме 0 в нашия пример
#info/ 9 добавяме като цифра, която искаме да бъде добавена
#info/ Отговор от двата примера [1,2,3,9] и [9,1,2,3,9]