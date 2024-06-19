# 1....................................................... 

# import multiprocessing as mp


# def worker (n):
#     res = n*1000
#     print(f'res in {mp.current_process().name} = {res}')

# if __name__ == "__main__":
#     process_number = 5 
#     process_pool =[]
# # worker(1)
# # worker(2)
# # worker(3)
# # worker(4)
# # worker(5)
#     for i in range (process_number):
#         pr = mp.Process(target=worker, args = (i,))
#         pr.start()
#         process_pool.append(pr)

 
# print("End")