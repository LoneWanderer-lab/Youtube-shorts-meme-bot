import os

def cleanup():
    for files in os.listdir("memes"):
        os.remove("memes/" + files)

    for files in os.listdir("newMemes"):
        os.remove("newMemes/" + files)