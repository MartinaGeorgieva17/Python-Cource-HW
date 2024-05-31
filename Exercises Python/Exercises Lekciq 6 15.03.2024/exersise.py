
#Primeri za split
#text = 'word1, word2, word3'
#words = text.split(', ')
#print (words)
#print(len(words))


#1.1 conzole from 1 to 10 / Variant 1
#print(1)
#print(2) 


#1.2./repeat 5 times for each value in[]

#for x in [1,2,3,4,5]:
 #   print(x)
#   print('END')


#1.3 RANGE изписва от даденото число до крайното, но без последното написано 
#for x in range(1,6):
 #  print(x)

#print('END')



#1.4 RANGE TASK: print 'hi' 5 times with cycles /ixpiswa deset poredni puti 'hi'
#for x in range(5):
 #  print('hi')


#1.5 Range 
#for _ in range(5):
 #   print('hi')


#1.6 Range (start,stop,step) /printira na edin red end ='',''
#range(stop) =>start = 0

#for x in range(5): 
#    print(x, end=",")

#1.7Range (start,stop,step) /printira na edin red end ='',''
#range(stop) =>start = 0


#for x in range (5, 1, -1):
  #  print(x, end=",") #otgovor 5,4,3,2


#1.8 Range .................
    
#for x in range (4,2, -1):
#    print(x, end=",") # otgovor 4,3

#1.9 Range упражнения 
#for x in range (8,1, -3):
 #   print(x, end=",") # otgovor 8,5,3, 


#1.10 Range ............
#for x in range (8,1, -3):
  #  print(x, end=",")

#Task: write range, print numbers 10, 8, 6, 4, 2
#for x in range(10, 1, -2):  #може и да са 10,0, -2 и получаваме 10,8,6,4,2
 # print(x, end=", ")


#2.00 for on sequences/ izrezhda vsichki a b c d

#text = 'abcd'
#for l in text: 
  #  print(l)

#2.1 nested for loops ...........


#range(1,4)
#1a, 1b, 1c - trqbva da polychim TASK 
#2a, 2b, 2c - trqbva da polychim TASK 
#3a, 3b, 3c - trqbva da polychim TASK 

#for num in range (1,4): 
 #   print(num, end=', ')

#dobavqme i cifrite i sglobqvame - reshenina task 


#stranichne primer izvuntask-a
#text = "abc"
#for l in text:
 #    for num in range(1,4):
 #       print(l+str(num), end=", ")
 #    print()



#otgovor na task 
#1a, 1b, 1c - trqbva da polychim TASK 
#2a, 2b, 2c - trqbva da polychim TASK 
#3a, 3b, 3c - trqbva da polychim TASK 


#text = "abc"
#for num in range(1,4):
  #  for l in text:
  #      print(str(num) + l, end=', ')
  #  print()



#3.0 Continue / propyska vsichko sled nego vslychaq propysa 2 

#for num in range(5):
 #   if num==2:
  #      print('@@@')
  #      continue
   # print(num)


#3.1 continue /TASK/ skipva 2-kite na predniq primer 

#text  = 'abc'
#for num in range(1,4):
 #   if num%2==0:
  #     continue

#for l in text:
#     print(str(num)+l, end= ", ")

#print()



#3.2 BREAK
#for num in range(5): 
  #  if num==3:
   #     print('Three')
   #     break
   # print(num)
#print('End')


#3.3  BREAK EXAMPLE
#text = 'abc'
#for num in range(1,4):
 #   if num%2==0:
 #       break
 #   for l in text:
 #       print(str(num)+l, end=",")
#print()


#3.4 PASS EXAMPLE 

#for x in range(5):
 #   pass


#3.5 While Example 
#For cycle - 
#kogato znaem kolko na broi 
#puti trqbva da se izpulni dadeno deistvie 
#
#Task:generate random number
#import random
#random_number = random.randint(1,10)
#print(random_number)


#3.6 WHILE 
#task if you know condition for l=iterrations => while loop 
#import random
#for _ in range(100):
 #   random_number = random.randint(1,100)
  #  print(random_number)
  #  if random_number%2==0:
   #    print('ok')
    #   break
#print('End')

#3.7 else in range 

#for num in range(1,6):
 #   print(num)
 #   if num ==3:
 #       break
#
#else:
 #   print('OK')



#3.8 While
#endless loop example
#while True:
 #   print('Ok')



#3.9 #While example:For user input 
#Task: let the user enter number (x). While the user enters x!= (razlichno ot chislo) numbers
#ask him/her to enter again 

#while True:
 #   try:
 #     x=int(input('x='))
 #     break
 #   except:
 #       print('Enter a nmuber!!!')

#print(f'bravo, x={x}')




#4.0 DALI V X IMAME CHISLO 
#x=2
#print(isinstance(x, int))





   