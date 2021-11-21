from pytube import Playlist

import ssl 
ssl._create_default_https_context = ssl._create_unverified_context

print("========================")
play_list_url = input("Please Enter the URL for the playlist: ")

playlist = Playlist(play_list_url)

# 顯示 playlist 裡面影片總數
print('Number of videos in playlist: %s' % len(playlist.video_urls))

# 顯示所有影片的 url
# print("========================")
# for video_url in playlist.video_urls:
#     print(video_url)

# 顯示所有影片的 title
# print("========================")
# for video in playlist.videos:
#     print(video.title)

# 顯示所有影片的資料內容
# print("========================")
# for video in playlist.videos:
    
    # 具有影訊和音訊的檔案
    # print(video.streams.filter(progressive=True))

    # 解析度為 720p 的檔案
    # print(video.streams.get_by_resolution('720p'))

    # 解析度為 720p 的檔案的 itag
    # print(video.streams.get_by_resolution('720p').itag)

for video in playlist.videos:
    resolution720_itag = video.streams.get_by_resolution('720p').itag
    video.streams.get_by_itag(resolution720_itag).download("/Volumes/PortableSSD/06_JavaWeb_JQuery/")

# 下載檔案
# for video in playlist.videos:
#     video.streams.get_by_itag(22).download("/Volumes/PortableSSD/HTML3_CSS3_148/")
