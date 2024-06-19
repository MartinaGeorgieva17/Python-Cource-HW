# from multiprocessing import Pool
# import time

# def worker (n):
#     return n*1000


# if __name__ == '__main__':
#     t = time.time()

# # Creeate the pool:
# p = Pool(processes=5)

# result = p.map(worker, range (100000))
# p.close()
# p.join()

# print('Pool took: ', time.time() -t)

# # serial processing:

# t = time.time()
# result=[]
# for x in range (100000):
#     result.append(worker(x))
#     # print("Result:", result)
# print ('Serial processing took:', time.time() - t)
