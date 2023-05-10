import moviepy.editor
import os
import random
import math
import cv2
import simpleYtUploader
from datetime import datetime


def videoS(txt, bgVid, videoNum):
    testVideoClip = moviepy.editor.VideoFileClip(bgVid)
    timestamp = math.floor(random.randint(1, math.floor(testVideoClip.duration - 6)))

    vidClips = []

    leng = 4
    videoA = moviepy.editor.VideoFileClip(bgVid).subclip(timestamp, timestamp + leng)
    textA = moviepy.editor.TextClip("Did You Know...", fontsize=50, bg_color='black', color='white', font='Calibri-Bold')
    text2A = textA.set_pos('center').set_duration(leng)
    video2A = moviepy.editor.CompositeVideoClip([videoA, text2A])
    timestamp += leng
    vidClips.append(video2A)

    leng = 2
    videoA = moviepy.editor.VideoFileClip(bgVid).subclip(timestamp, timestamp + leng)
    textA = moviepy.editor.TextClip(txt, fontsize=40, bg_color='black', color='white', font='Calibri-Bold')
    text2A = textA.set_pos('center').set_duration(leng)
    video2A = moviepy.editor.CompositeVideoClip([videoA, text2A])
    timestamp += leng
    vidClips.append(video2A)

    videoC = moviepy.editor.concatenate_videoclips(vidClips)

    audio = moviepy.editor.AudioFileClip('C:\\Users\\18043\\PycharmProjects\\DYK Video Handler\\audio_files\\music.mp3')
    num = math.floor(random.randint(1, math.floor(audio.duration - videoC.duration)))
    audio = audio.subclip(num, num+videoC.duration)
    audio = audio.volumex(0.05)
    videoC = videoC.set_audio(audio)
    name = "Did you know...    #facts #funfacts "+str(videoNum)
    location = f'C:\\Users\\18043\\PycharmProjects\\DYK_Video_Handler\\NewVideos\\'+name + '.mp4'
    videoC.write_videofile(location)
    return location, name


def split_text(text, x=20):
    words = text.split()
    substrings = []
    current_substring = ""

    for word in words:
        if len(current_substring) + len(word) + 1 <= x:
            if current_substring:
                current_substring += " "
            current_substring += word
        else:
            substrings.append(current_substring)
            current_substring = word

    substrings.append(current_substring)
    result = "\n".join(substrings)
    return result


def makeVid():
    vnum = 0
    directory_path = "C:\\Users\\18043\\PycharmProjects\\DYK_Video_Handler\\BackgroundVideos\\short"
    all_files = os.listdir(directory_path)

    f = open("facts/facts.txt", "r", encoding="utf-8")
    for fact in f:
        fact.strip()
        fact = split_text(fact.replace('\n', ''))
        vnum += 1
        bgVideo = "C:\\Users\\18043\\PycharmProjects\\DYK_Video_Handler\\BackgroundVideos\\short\\"+random.choice(all_files)
        videoS(fact, bgVideo, vnum)


def chooseVid(vnum):
    directory_path = "C:\\Users\\18043\\PycharmProjects\\DYK_Video_Handler\\BackgroundVideos\\short"
    all_files = os.listdir(directory_path)
    fact_list = []
    f = open("C:\\Users\\18043\\PycharmProjects\\DYK_Video_Handler\\facts\\ExtraWellSizedFacts.txt", "r", encoding="utf-8")
    for fact in f:
        fact.strip()
        fact = split_text(fact.replace('\n', ''))
        fact_list.append(fact)
    fact = random.choice(fact_list)
    vnum += 1
    bgVideo = "C:\\Users\\18043\\PycharmProjects\\DYK_Video_Handler\\BackgroundVideos\\short\\" + random.choice(all_files)
    local, title = videoS(fact, bgVideo, vnum)
    return local, title


def getFirstFrame(videoFile):
    vidCap = cv2.VideoCapture(videoFile)
    success, image = vidCap.read()
    if success:
        cv2.imwrite("C:\\Users\\18043\\PycharmProjects\\DYK_Video_Handler\\thumbnailPackage\\first_frame.jpg", image)
    else:
        raise Exception("failed frame extraction")
        # quit()
    return "C:\\Users\\18043\\PycharmProjects\\DYK_Video_Handler\\thumbnailPackage\\first_frame.jpg"


def clear(directory_path):
    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)
        try:
            if os.path.isfile(file_path):
                os.remove(file_path)
        except Exception as e:
            print(f"Error deleting file: {file_path} - {e}")


def uploader():
    vidDirectory = "NewVideos"
    vid_files = os.listdir(vidDirectory)
    for vid in vid_files:
        vidPath = "C:\\Users\\18043\\PycharmProjects\\DYK_Video_Handler\\NewVideos\\"+vid
        vidTitle = vid[:-4]
        thumbnail = getFirstFrame(vidPath)
        simpleYtUploader.upload(vidPath, vidTitle, thumbnail)


with open('C:\\Users\\18043\\PycharmProjects\\DYK_Video_Handler\\log.txt', 'a') as file:
    file.write(f'file ran at {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')


for x in range(3):
    with open('C:\\Users\\18043\\PycharmProjects\\DYK_Video_Handler\\vnum.txt', 'r') as file:
        vnum = int(file.read())
    path, name = chooseVid(vnum)
    simpleYtUploader.upload(path, name, getFirstFrame(path))
    with open('C:\\Users\\18043\\PycharmProjects\\DYK_Video_Handler\\vnum.txt', 'w') as file:
        file.write(str(vnum+1))

with open('C:\\Users\\18043\\PycharmProjects\\DYK_Video_Handler\\log.txt', 'a') as file:
    file.write(f', File ran sucessfully \n')