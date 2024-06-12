# 1....................................

# import threading
# import time 

# def worker (num):
#     print(f'Worker{num} starting')
#     # Simulate some work 
#     time.sleep(2)
#     print(f'Worker {num} done')

# if __name__ =='__main__':
#     start = time.time()
#     threads = [] 

#     for i in range (5):
#         t = threading.Thread(target=worker, args = (i,))
#         threads.append(t)
#         t.start()

#     for t in threads:
#             t.join()

#     end = (f'time:{end-start}')




# 2...Threading ...................................................

# import threading

# def count():
#     global x;
#     x+=1
#     print(f'x={x}')


# x=0
# tr1=threading.Thread(target=count)
# tr1.start() #count()





# 3.Thread.....................

# def Thread(target):
#     print('Thread called')
#     print(target)

# def count():
#     print('Count is called')

# Thread (count())
# print('End')






# 4.Thread Example......................................

# def thread(target=None, name=None, demon=None):
#     print('Thread called')
#     target()

# def count():
#     print('Count is called')

# thread (count, 'T1', True)
# thread(name='T1', demon=True, target=count)
# print('End')






# 5...............................................

# import threading
# import time

# def Thread(target):
#     print('Thread called')
#     print(target)

# def worker():
#     time.sleep(0.5)
#     print('Worker is called')

# print(1)
# tr1 = threading.Thread(target=worker)
# print(2)

# tr1.start()
# print(3)




# 6..........................................................

# import threading
# import time


# def worker():
#     time.sleep(0.5)
#     print(f'Worker is called in thread {threading.current_thread().name}')


# tr1 = threading.Thread (target =worker, name = 'Tr1')
# tr2 = threading.Thread(target=worker, name='Tr2')

# print(1)
# tr1.start()
# tr2.start()

# print(2)




# 7..Thread with args Example
# ..........................................................


# import threading
# import time


# def worker(x):
#     time.sleep(0.5)
#     print(f'Worker is called in thread {threading.current_thread().name}')


# tr1 = threading.Thread (target =worker, args=(1,))
# tr2 = threading.Thread(target=worker, args=(2,))

# print(1)
# tr1.start()
# tr2.start()

# print(2)




# 8.Example threads with keywords (kwargs)..........................................


# import threading
# import time


# def worker(x):
#     time.sleep(0.5)
#     print(f'Worker is called in thread {threading.current_thread().name}')

# threading.Thread(target=None)
# tr1 = threading.Thread (target =worker, args=(1,))
# tr2 = threading.Thread(target=worker, kwargs ={'x':2})

# print(1)
# tr1.start()
# tr2.start()

# print(2)




# 9..Exmple from old stuff in lectures ..........

# def foo(*args, **kwargs):
#     print(args)
#     print(kwargs)

# foo(1,2,3)



# 10..Threads Example............................................


# import threading
# import time


# def worker():
#     time.sleep(1)
#     print(f'Worker is called in thread {threading.current_thread().name}')

# tr1 = threading.Thread (target =worker)
# tr2 = threading.Thread (target =worker)

# start = time.time()
# tr1.start()
# tr2.start()
# end=time.time()

# print(f'time:{end-start}')



# 11...........................................
# Join Example (изчаква)..........................................................

# import threading
# import time


# def worker():
#     time.sleep(1)
#     print(f'Worker is called in thread {threading.current_thread().name}')


# tr1 = threading.Thread (target =worker)
# tr2 = threading.Thread (target =worker)


# start = time.time()
# tr1.start()
# tr2.start()

# tr1.join()
# tr2.join()
# end=time.time()

# print(f'time:{end-start}')



# 12..........................................................

# import threading
# import time

# max_range = 10_000_000
# max_range_half = max_range//2

# def worker(r):
#     tid = threading.current_thread().name

#     global result
#     res = 0

#     for i in r:
#         res+=1

#     result +=res
#     print(f'Worker{tid} is working with {r}')


# t = time.time()
# result = 0

# worker(range(max_range_half))
# worker(range(max_range_half, max_range))

# print('Sequential Processing result: ', result)
# print('Sequential Processing took: ', time.time() -t, "n")

# t = time.time()
# result = 0 

# tr1 = threading.Thread(target =worker, args= (range(max_range_half),))
# tr2 = threading.Thread(target =worker, args= (range(max_range_half, max_range),))
                       
# tr1.start(); tr2.start()
# tr1.join(); tr2.join()

# print('Multithreaded Processing Result:', result)
# print('Multithreaded Processing Took:', time.time() - t, 'n')





# 13..Критична секция ....................................................
# Lock the cretical section

# import threading

# def worker(lock):
#     global counter

#     for i in range(1_000_000):
#         counter +=1

# counter =0
# lock = threading.Lock()

# thread_pool =[]
# for i in range(2):
#    tr = threading.Thread(target=worker, args = (lock,))
#    thread_pool.append(tr)

#    print(f'Counter before starts of {tr.name}: {counter}')
#    tr.start()

# for tr in thread_pool:
#     tr.join()

# print('Workers counted:', counter)




# 14........................................................
# Multiprocessing Threding 

import threading
import multiprocessing
import time

def worker (num):
    print(f'Worker {num} starting')
# Simulate some work
    time.sleep(2)
    print(f'Worker {num} done')

def concequently():
    start = time.time()
    for i in range (5):
        worker(i)

    end = time.time()
    print(f'concequently execution time: {end-start}')



def threading_demo():
    start = time.time()
    process=[]

    for i in range(5):
        p = threading.Thread(target=worker, args = (i, ))
        process.append(p)
        p.start()

    for p in process:
        p.join()

    end = time.time()
    print(f'threading_demp time: {end-start}')


def multiprocessing_demo():
    start = time.time()
    process = []

    for i in range (5):
        p = multiprocessing.Process(target=worker, args = (i, ))
        process.append(p)
        p.start()

    for p in process:
        p.join()

    end = time.time()
    print(f'threaded execution time: {end-start}')

 
if __name__ == '__main__':
    concequently()
    threading_demo()
    multiprocessing_demo()

