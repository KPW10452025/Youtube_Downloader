# MAC 執行爬蟲時需要的必須程序
import ssl 
ssl._create_default_https_context = ssl._create_unverified_context

# 從 pytube 裡面調用 YouTube
from pytube import YouTube

yt = YouTube('https://youtu.be/jN-ttNTKers')

# 使用 .title 可以得到影片的標題
print(yt.title)
# 039 尚硅谷 爬虫 字典的高级 修改

# 將 mp4 的檔案打印出來
for i in yt.streams.filter(file_extension='mp4'):
    print(i)

# 下載 itag=22 的檔案
iteam = yt.streams.get_by_itag(22)
print(iteam)
iteam.download()
