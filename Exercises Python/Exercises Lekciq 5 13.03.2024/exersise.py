#1 input

#print('hi')
#user_name = input("Enter your name:")
#print(f'user_name:{user_name}')
#print('End')

#2 input проверка на тип данни str в int 
#x = input('x=')
#print(type(x))
#print(f'x*3={x*3}')


#3.
#a = '5.5'
#print(float(a))

#4. int, input
#x = input('x=')
#print(type(x))
#x= int(x)
#print(type(x))
#print(f'x*3={x*3}')

#5. int , input int - polycjavame cqlo chislo 
#x=int(input('x='))
#print(f'x*3={x*3}')

#6. Primerna zadacha za izpit 
#print(bool(-3.25)) #true
#if -3.25:
 #   print('hi')


#7.  x - ostava string, zaradi tova vrushta string 
#x = input('x=')  
#res = int(x)*2
#print(res)

#print(type(x))


#8. #fynkciqta 'int' ne moje da napravi ot simvolite celi chisla ili ot ne celite;

#x = int(input('x=')) 
#print(x*3)


#9.................
#print(int('3'))
#print(ord('3'))    #ASCII tablica vrushta otgovor 51

#ord vrushta koda 

#print(chr(465))    #vrusha simvol 


#10. int.......................

#print(int('0101', base=2)) #dava dvoichna sistema chrez base=2


#11. Hvahstane na greshki/Exception/Error Handling................

#potrebitelqt iska da vuvede edno cqlo chislo/greshki 
#11.1
#x = int(input('Enter number:'))
#print(f'x*2={x*2}') #a runtime error
#11.2
#x = '3's # syntax error

#11.3...........................

#try:
 #  x = int(input('Enter number:'))
 #  print(f'x*2={x*2}')
#except:
 #  print('Enter a number!')
#print('End')


#11.4 input error..........................

#input(ctrl+c:)


#12.0 Errors .....................
#print(3/0) # ne mozhem da delim na 0
#print(x) #name error
#int('pesho') #value error - pesho 
  

#12.1 input....................
#try:
  # x=int(input('x':))
  # print(f'x={x}')
  # print(3/x)

#except ValueError:
#print('Must be number')

#except ZeroDivisionError:
#print('I can not divide by 0!')

#except:
#print('OOPS,something went wrong...')


#13.0 print ...................

#print(1,2,3) #1 2 3
#print(1,2,3, sep=';') #1;2;3

#13.1 print......................
#print(1, end=' ') # 1  2
#print(2)

#13.2 print...............
#print(1)  # 1 i na nov red 2
#print(2)

#13.3 print.............
#print(1, end=' ')
#print(2, end=' ') # otgovor 1 2 3 
#print(3)

#14.0 Zadachi za yprajneniq ot domashnoto

#Zadacha 1/Lekciq 5....................
#x ='1234' # ako iskame da vzemem purviq simvol 
#print( x[0], x[3]) #broeneto zapochva ot  nyla


try:
    #x = int(input('x:'))
    x='3332'
    first = int(x[0] + x[3])
    second = int(x[1] + x[2])
    x = int(x)

    if not 1000<=x<=9999:
        print('Enter a 4 digit number')
        exit()   
    print('Your code here:')
except:
    print('Enter a number')
        





