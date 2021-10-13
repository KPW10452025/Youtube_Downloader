# MAC 執行爬蟲時需要的必須程序
import ssl 
ssl._create_default_https_context = ssl._create_unverified_context

# 從 pytube 裡面調用 YouTube
from pytube import YouTube

# 製作一個功能：能在 terminal 輸入 URL
video_url = input("Please Enter the URL ofr the video: ")

# 輸入完 URL 後顯示如下
print("Processing, please wait...")

# 讓系統開始分析
yt = YouTube(video_url)
# 讀取影片標題
video_title = yt.title
# 塞選影片
video_streams = yt.streams.get_by_itag(22)
# video_streams = yt.streams.filter(progressive=True)
# progressive=True 只的是此檔案同時擁有影像檔與影音檔

# 由於下載影片要花時間，所以先顯示系統提示後再使用 .download()
print("Downloading( {} ), please wait... ".format(video_title))
video_streams.download()
print("Download Complete.")
