import os
import praw
import requests
from datetime import datetime

def downloadMemes():
    #gets reddit credentials
    r = praw.Reddit(client_id = 'Your own client ID', 
                         client_secret = 'Your own client secret', 
                         user_agent = 'Your own user agent')

    #checks integrity of output folders
    if os.path.exists("memes"):
        pass
    if not os.path.exists("memes"):
        os.mkdir("memes")

    if os.path.exists("newMemes"):
        pass
    if not os.path.exists("memes"):
        os.mkdir("newMemes")

    #gets subreddit and number of posts depending on the day of the week
    dt = datetime.now()
    day = dt.weekday()
    if day == 0:
        subreddit = r.subreddit('Memes')
        posts = subreddit.hot(limit=9)
    if day == 1:
        subreddit = r.subreddit('dankmemes')
        posts = subreddit.hot(limit=9)
    if day == 2:
        subreddit = r.subreddit('AnarchyChess')
        posts = subreddit.hot(limit=9)
    if day == 3:
        subreddit = r.subreddit('ProgrammerHumor')
        posts = subreddit.hot(limit=9)
    if day == 4:
        subreddit = r.subreddit('school_memes')
        posts = subreddit.hot(limit=9)
    if day == 5:
        subreddit = r.subreddit('wholesomememes')
        posts = subreddit.hot(limit=9)
    if day == 6:
        subreddit = r.subreddit('AnimalMemes')
        posts = subreddit.hot(limit=9)

    #Downloads the posts
    for post in posts:
        url = (post.url)
        file_name = url.split("/")
        file_name = file_name[-1]
        print(file_name)
        r = requests.get(url)

        with open("memes/" + file_name,"wb") as f:
            f.write(r.content)

downloadMemes()
