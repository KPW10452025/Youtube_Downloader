from pytube import Playlist

import ssl 
ssl._create_default_https_context = ssl._create_unverified_context

playlist = Playlist("https://youtube.com/playlist?list=PLmOn9nNkQxJFs5KfK5ihVgb8nNccfkgxn")

print('Number of videos in playlist: %s' % len(playlist.video_urls))

# 顯示所有影片的 url
# for video_url in playlist.video_urls:
#     print(video_url)

# 顯示所有影片的 title
# for video in playlist.videos:
#     print(video.title)

for video in playlist.videos:
    video.streams.get_by_itag(22).download("/Volumes/PortableSSD/HTML3_CSS3_148/")

# 參考資料
# https://jbprogramnotes.com/2021/07/%E4%BD%BF%E7%94%A8-pytube-%E5%A5%97%E4%BB%B6%E4%B8%8B%E8%BC%89-youtube-%E5%BD%B1%E7%89%87/
# https://liaozihzrong.github.io/2020/08/14/allinone19/
# https://stackoverflow.com/questions/54710982/using-pytube-to-download-playlist-from-youtube
