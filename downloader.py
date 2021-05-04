#=====================================================
# Command Line Version.(Linux Only)
#=====================================================
# import os
#
# downloadList = open("list.txt", "r+").readlines()
# for link in downloadList:
#     try:
#         print("Downloading {}...".format(link))
#         os.system("youtube-dl -f bestaudio --extract-audio --audio-format mp3 \
#     --audio-quality 0 {}".format(link))
#     except Error as e:
#         with open("failed.txt", "w+") as failed:
#             failed.writeline(link, "\t", e)
#=====================================================
#
#
#=====================================================
# Python Library Version.(Cross Platform)
#=====================================================

from __future__ import unicode_literals
import youtube_dl


class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)


def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')


ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '320',
    }],
    'logger': MyLogger(),
    'progress_hooks': [my_hook],
}

links = open("linksList.txt", "r+").readlines()

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    for link in links:
        ydl.download([link])
