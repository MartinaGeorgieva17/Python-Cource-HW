# 1...............................................


# import time

# def download_video(url):
#     time.sleep(1)
#     print(f'{url} is downloaded!')

# video_url =[
#     'url1',
#     'url2',
#     'url3',
#     'url4',
#     'url5',
# ]

# start = time.time()
# for url in video_url:
#     download_video(url)

# time_taken = time.time() - start
# print(f'Time taken:{time_taken}')





# 2...............С тредове същата задача .............

# import time
# import threading

# def download_video(url):
#     time.sleep(1)
#     print(f'{url} is downloaded!')

# video_url =[
#     'url1',
#     'url2',
#     'url3',
#     'url4',
#     'url5',
# ]

# start = time.time()
# threads= []

# for url in video_url:
#     tr = threading.Thread(target =download_video, args =(url,))
#     tr.start()
#     threads.append(tr)
   
# # make sure that all threads are finished their job   
# for tr in threads:
#     tr.join()
    

# time_taken = time.time() - start
# print(f'Time taken:{time_taken}')

# # sequential time: time_taken