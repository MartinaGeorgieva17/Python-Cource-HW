
# 1.......Теглене на видеа от YouTube..........................


# >>> from pytube import YouTube
# >>> YouTube('https://youtu.be/9bZkp7q19f0').streams.first().download()
# >>> yt = YouTube('http://youtube.com/watch?v=9bZkp7q19f0')
# >>> yt.streams
# ... .filter(progressive=True, file_extension='mp4')
# ... .order_by('resolution')
# ... .desc()
# ... .first()
# ... .download()



# 2..Example...............................................

# class Streams:
#     def first(self):
#         print('first on streams is called')

# class YouTube:
#     def __init__(self, video_url)->None:
#         self.video_url = video_url
#         print('An object is created!')

#         self.streams = Streams()

# # YouTube('https://youtu.be/9bZkp7q19f0').streams.first()
# # videi_obj = Youtube('url')
# # video_obj.streams.first()

# YouTube('url').streams.first()




# 3.Example for downloading video from youtube..........................................



# from pytube import YouTube

# YouTube('https://youtu.be/ea9fCSXGhSU?feature=shared').streams.first().download()




# 4...Download Video Example 2................................................

# from pytube import YouTube

# yt = YouTube ('https://youtu.be/ea9fCSXGhSU?feature=shared')
# print(f'author: {yt.author}')
# print(f'fmt_streams:{yt.fmt_streams}')




# 5...Download Video Example..........................................................


# from pytube import YouTube

# pl = Playlist('https://www.youtube.com/watch?v=qM9UJ8QlV94&list=FL3eaXPePxoYZ5_0cFElG2tA')

# print(f'Videos count: {pl.length}')

# for video_url in pl.url_generator():
#     print(video_url)
 


# 6.................................................