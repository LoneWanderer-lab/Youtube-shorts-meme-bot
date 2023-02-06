import os
from simple_youtube_api.Channel import Channel
from simple_youtube_api.LocalVideo import LocalVideo

def upload_video():
    # loggin into the channel
    channel = Channel()
    channel.login("client_secret.json", "credentials.storage")

    # setting up the video that is going to be uploaded

    video = LocalVideo(Output_Video="test_vid.mp4")

    # setting snippet
    video.set_title("My Title")
    video.set_description("This is a description")
    video.set_tags(["funny", "memes", "subscribe"])
    video.set_category("memes")
    video.set_default_language("en-US")

    # setting status
    video.set_embeddable(True)
    video.set_license("creativeCommon")
    video.set_privacy_status("public")
    video.set_public_stats_viewable(True)

    # uploading video and printing the results
    video = channel.upload_video(video)