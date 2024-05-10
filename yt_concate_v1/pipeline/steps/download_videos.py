from pytube import YouTube
from pytube.innertube import _default_clients

_default_clients["ANDROID_MUSIC"] = _default_clients["ANDROID_CREATOR"]   #解決AgeRestrictedError問題

from yt_concate_v1.pipeline.steps.step import Step
from yt_concate_v1.settings import VIDEOS_DIR

class DownloadVideos(Step):
    def process(self, data, inputs, utils):
        # print(len(data))
        yt_set = set([found.yt for found in data])  #set的作用為把重複的yt(captions)給刪除
        print("videos to download=", len(yt_set))
        for yt in yt_set:  #found = Found(yt, text, time)
            url = yt.url

            if utils.video_file_exists(yt):
                print(f"found existing video file for {url}, skipping")
                continue
            print("downloading", url)
            # try:
            # except:
            YouTube(url).streams.first().download(output_path=VIDEOS_DIR, filename=yt.id + ".mp4")
        return data