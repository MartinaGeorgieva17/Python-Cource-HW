# import requests
# import os
# import time


# def download_file(url):
#     file_name =url.split('/')[4]+'.jpg'

#     full_file_name = os.path.join(download_path, file_name)

#     # get imagee bytes

#     print(f"Start donwloading {url}")
#     response = requests.get(url, allow_redirects=True)

# # write image to file
#     try:
#         with open(full_file_name, 'wb') as fh:
#             fh.write(response.content)
#             print(f"File saved to {full_file_name}")
#     except FileNotFoundError:
#         os.mkdir(download_path)

# urls = [
#     'https://unsplash.com/photos/a-bowl-of-soup-with-the-letter-s-in-it-0Kst03fNbZs', 
#     'https://unsplash.com/photos/a-room-with-a-white-wall-and-a-white-chair-hmcNefbrr64',
#     'https://unsplash.com/photos/a-woman-in-an-orange-dress-standing-in-front-of-a-mountain-EPTk9I65EmM',
#     'https://unsplash.com/photos/a-living-room-with-a-couch-chair-table-and-a-large-poster-anWiq-JsgCg'

# ]

# download_path =os.path.join(os.getcwd(), "downloaded_images")


# if __name__ == '__main__':
#     start = time.perf_counter()

#     for url in urls:
#         download_file(url)
    

#     end = time.perf_counter()

#     print(f"Processing time: {end-start}")

