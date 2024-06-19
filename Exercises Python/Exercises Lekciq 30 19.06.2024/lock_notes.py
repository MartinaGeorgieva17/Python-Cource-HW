
# import threading

# def worker():
#     global x


# # Вариант 1:
#     # lock.aquire()
#     # try:
#     #     x+=1
#     # except:
#     #     print('An error occured')

#     # finally:
#     #     lock.release()

# # Вариант 2:
#     with lock:
#         try:
#             x+=1
#         except:
#             print('An error occured')

        


# if __name__=="__main__":
#     x=0
#     lock = threading.Lock()

#     tr1 = threading.Thread(target= worker)
#     tr2 = threading.Thread(target=worker)

#     tr1.start()
#     tr2.start()

#     tr1.join(x)
#     tr2.join(x)

#     print(f'Final value of x: {x}')

# # e еквивалентно по функционалност на:
# # some_lock.acquire()

#     # try:
#     #     # do something
#     # finally:
#     #     some_lock.release()