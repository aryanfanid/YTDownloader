from __future__ import unicode_literals
import youtube_dl
import PySimpleGUI as sg
from random import randrange

DOWNLOAD_DIR = '/home/aryanfanid/Desktop'

# Add a touch of color
theme_name_list = sg.theme_list()
sg.theme(theme_name_list[randrange(len(theme_name_list))])

# All the stuff inside your window.
layout = [[sg.Text('YouTube URL:'), sg.InputText()],
          [sg.Text('Download Directory:'), sg.InputText(
              default_text=DOWNLOAD_DIR)],
          [sg.Button('Download'), sg.Button('Cancel'), sg.Text('', key='-ds-')]]

# Create the Window
window = sg.Window('YouTube Downloader', layout)


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

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([values[0]])

window.close()
