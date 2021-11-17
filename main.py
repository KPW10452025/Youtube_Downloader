# MAC 執行爬蟲時需要的必須程序
import ssl 
ssl._create_default_https_context = ssl._create_unverified_context

# 從 pytube 裡面調用 YouTube
from pytube import YouTube

# 製作進度條
from pytube.cli import on_progress

# 製作一個功能：能在 terminal 輸入 URL
print("=============================================")
video_url = input("Please Enter the URL for the video: ")

# 輸入完 URL 後顯示如下
print("Processing, please wait...")

# 讓系統開始分析
yt = YouTube(video_url, on_progress_callback=on_progress)
# 讀取影片標題
video_title = yt.title
# 塞選影片
video_streams = yt.streams.get_by_itag(22)
# video_streams = yt.streams.filter(progressive=True)
# progressive=True 只的是此檔案同時擁有影像檔與影音檔
# for video_stream in video_streams:
    # print(video_stream)

# 檢視欲下載檔案的內容
print("=============================================")
print("File name( {} )".format(video_title))
print("File information: ", video_streams)

check_point = input("Press 1 to download. Press 2 to stop: ")
if int(check_point) == 1:
    # 由於下載影片要花時間，所以先顯示系統提示後再使用 .download()
    print("=============================================")
    print("Downloading( {} ), please wait... ".format(video_title))
    video_streams.download("/Volumes/PortableSSD/HTML3_CSS3/")
    print("Download Complete.")
else:
    pass

#  /Volumes/PortableSSD/Youtube/Python_Web_Scrapying 
