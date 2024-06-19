# 1..................................

# import time
# import multiprocessing

# def download_video(url):
#     time.sleep(1)  # Simulating download time
#     print(f'{url} is downloaded!')

# if __name__ == '__main__':
#     video_urls = [
#         'url1',
#         'url2',
#         'url3',
#         'url4',
#         'url5',
#     ]

#     start = time.time()
#     processes = []
    
#     for url in video_urls:
#         pr = multiprocessing.Process(target=download_video, args=(url,))
#         pr.start()
#         processes.append(pr)
    
#     # Ensure all processes have finished their job
#     for pr in processes:
#         pr.join()
    
#     time_taken = time.time() - start
#     print(f'Total time taken: {time_taken} seconds')

# # sequential time: time_taken



# 2...................................

# import multiprocessing as mp

# # Global variable
# x = 0

# def increment(r):
#     global x
#     for _ in r:
#         x += 1
#     print(f'x in {mp.current_process().name}: {x}')

# if __name__ == '__main__':
#     X = 0
    
#     pr1 = mp.Process(target=increment, args=(range(1000),))
#     pr2 = mp.Process(target=increment, args=(range(1000),))

#     pr1.start()
#     pr2.start()

#     pr1.join()
#     pr2.join()

#     print(f'x in {mp.current_process().name}: {x}')




# Друг вариант за решаване на задачата: 


# import multiprocessing as mp
# import time

# def increment(queue, r):
#     x = queue.get()

#     print(f'x in process{mp.current_process().name} ={x}')

#     for _ in r:
#         x += 1


# # save to queue incremented x:
#     queue.put(x)
#     print(f'x in {mp.current_process().name}: {x}')


# if __name__ == '__main__':

#     queue = mp.Queue()
#     queue.put(0)


#     start=time.time()
#     pr1 = mp.Process(target=increment, args=(queue, range(1000),))
#     pr2 = mp.Process(target=increment, args=(queue, range(1000),))


#     pr1.start()
#     pr2.start()
#     pr1.join()
#     pr2.join()
    
#     x = queue.get()
#     time_taken = time.time() - start
#     print(f"x in process {mp.current_process().name}: {x}")
#     print(f"Time taken: {time_taken} seconds")



# 3..FIFO, LIFO (first in, first out - FIFO) last in first out (LIFO)..................................

# FIFO = first in first out 

# LIFO = last in first out 


# 1,2,3 => FIFO => 1,2,3
# 1,2,3 => LIFO => 3,2,1


# 4. Създаване и сартиране на процес: 

# import multiprocessing as mp
# import time 

# def worker(x):
#     pi = mp.current_process().name;
#     print('x={} in {}'. format (x,pid))
#     time.sleep(2)

# if __name__ =="__main__":
#     p = mp. Process(target = worker, args=(42, ))
#     p.start
#     p.join
#     print('Worker did its job as separate Process!')


# 5....................