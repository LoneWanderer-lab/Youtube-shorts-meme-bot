import os
from PIL import Image
from moviepy.editor import AudioFileClip, ImageClip, concatenate_videoclips

def makeVideo():
    m = 0
    finalMemes = []
    imageSize = 1920, 1920
    Audio = AudioFileClip("video_assets/music.mp3")

    #gives all the memes a duration, resizes them and appends them to a list
    for pictures in os.listdir("memes"):
        m = m+1
        images = Image.open("memes/" + pictures)
        newMemes = images.resize((imageSize))
        newMemes.save("newMemes/" + pictures)

    for clips in os.listdir("newMemes"):
        clips = ImageClip("newMemes/" + clips, duration=6)
        finalMemes.append(clips)

    #calculates the audio durations
    amountMemes = len(finalMemes)
    audioTime = amountMemes * 6

    #gets name and exports the video
    name = input("Name:")
    frames = concatenate_videoclips(finalMemes, method="compose")
    getAudio = frames.set_audio(Audio).subclip(0, audioTime)
    finalVideo = getAudio.resize(height = 1920, width = 1080)
    finalVideo.write_videofile("Output_Video/" + name + '.mp4', fps=24, threads=4)




