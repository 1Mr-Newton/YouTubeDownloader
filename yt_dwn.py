import os
from pytube import YouTube
import shutil
from moviepy.editor import *


def merge():
  video_title = os.listdir('downloads/video')[0]
  if not video_title.endswith('.mp4'):
    pre,ext = os.path.splitext(video_title)
    os.rename(video_title, pre + '.mp4')


  video_path = f'downloads/video/{video_title}'
  audio_title = os.listdir('downloads/audio')[0]
  audio_path = f"downloads/audio/{audio_title}"
  final_path = f"downloads/{video_title}"



  videoclip = VideoFileClip(video_path)
  audioclip = AudioFileClip(audio_path)
  new_audio = CompositeAudioClip([audioclip])
  videoclip.audio = new_audio
  videoclip.write_videofile(final_path)

  shutil.rmtree('downloads/video')
  shutil.rmtree('downloads/audio')

url = input('Please provide the video url:\n')
# url = 'https://youtu.be/ZUdCm3jyL_c'
quality = input('Choose resolution "1080p", "720p","144p":\n')
resolutions = ['1080p','720p', '360p', '480p', '144p']

def videoDownloader(url,quality):
  yt = YouTube(url)
  try:
    yt.streams.filter(res=quality)[0].download('downloads/video/')
  except:
    yt.streams.get_highest_resolution().download('downloads/video/')

  yt.streams.get_audio_only().download('downloads/audio/')
  merge()
if quality not in resolutions:
  print('Watch carefully and choose one of the above resolutions')
else:
  videoDownloader(url, quality)



