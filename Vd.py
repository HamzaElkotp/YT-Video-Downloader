import os
from pafy import new
import time

#create save file section
try:
    os.makedirs("Downloads")

except OSError:
    if not os.path.isdir("Downloads"):
        raise
os.chdir("Downloads")

#downloadingbar
downlink = new(input('Enter file link to download it:'))
print('Title is: ',downlink.title)

#Video download section
def VideoD():
    qulity = downlink.streams
    X = -1
    for q in qulity:
        X += 1
        print('Video Quality {}'.format(X), q)
    qulity[int(input('Enter video quality here :'))].download()

#Audio download section
def AudioD():
    audio = downlink.audiostreams
    V = -1
    for r in audio:
        V += 1
        print('Audio Quality {}'.format(V), r)
    audio[int(input('Enter video quality here :'))].download()
    print('Download finished>>>')

#choose user option input V/A/B
print('Choose option V for downloading only video or B for video and audio ')
UserInput = input('Enter option:')
if UserInput == 'V':
    VideoD()
elif UserInput == 'B':
    VideoD()
    AudioD()
else:
    raise Exception('Error603, strange input')
print()
time.sleep(8)






#print(downlink)
#print('Title is: ',downlink.title)