from pytube import YouTube
from pytube.cli import on_progress
import sys
import ssl 
ssl._create_default_https_context = ssl._create_unverified_context

def interface():

    # Welcome
    print("Welcome to Pytube Downloader!")

    # Input the url
    url = input("Please input the url: ")
    print("Processing, please wait...")
    print(" ")

    # Response to the uel
    yt = YouTube(url, on_progress_callback=on_progress)
    for yt_stream in yt.streams:
        print(yt_stream)

    # Choose the itag
    print(" ")
    itag = input("Please choose the itag: ")
    download_itag = yt.streams.get_by_itag(itag)

    # Check the itag is exist
    if download_itag:
        print(" ")
        print("The itag you chose is {}.".format(itag))
        print("{} itag's information: ".format(itag))
        print(download_itag)
    else:
        print(" ")
        sys.exit("Please choose correct itag.")

    print(" ")
    print("Are you sure to download this file?")
    check_download = input("1 to Yes, 2 to No: ")

    if check_download == "1":
        yt_title = yt.title
        print("Downloading( {} ), please wait... ".format(yt_title))
        yt.streams.get_by_itag(itag).download()
        print("Download Complete.")
    else:
        print(" ")
        sys.exit("Please choose correct number.")



interface()
