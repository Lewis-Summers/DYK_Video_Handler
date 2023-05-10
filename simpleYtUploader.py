from simple_youtube_api.Channel import Channel
from simple_youtube_api.LocalVideo import LocalVideo


def upload(path, title, thumbnail, cat=24):
    video = LocalVideo(file_path=path)
    video.set_title(title)
    video.set_description(desc)
    # video.set_tags(["this", "tag"])
    video.set_category(cat)
    video.set_default_language("en-US")
    video.set_embeddable(True)
    # video.set_license("Standard YouTube License")
    video.set_privacy_status("public")
    video.set_public_stats_viewable(True)
    # setting thumbnail
    video.set_thumbnail_path(thumbnail)
    channel.upload_video(video)


channel = Channel()
channel.login("C:\\Users\\18043\\PycharmProjects\\DYK_Video_Handler\\YOUR_CLIENT_SECRET_FILE.json", "C:\\Users\\18043\\PycharmProjects\\DYK_Video_Handler\\credentials.storage")
desc = '''
Music: Runaway by Beau Walker is licensed under a Creative Commons License.
https://creativecommons.org/licenses/...
Support by RFM - NCM: https://bit.ly/3DAaboO
'''

