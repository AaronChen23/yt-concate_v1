import os
import json
from youtube_transcript_api import YouTubeTranscriptApi


from yt_concate_v1.pipeline.steps.step import Step


class DownloadCaptions(Step):
    def process(self, data, inputs, utils):  #data=video_links
        # for url in data:   #url=https://www.youtube.com/watch?v=j8KEkn04n3Y
        for yt in data:  # url=https://www.youtube.com/watch?v=j8KEkn04n3Y
            print("downloading caption for", yt.id)
            if utils.caption_file_exists(yt):
                print("found existing caption file")
                continue
            id = yt.url.split("?v=")[-1]
            try:
                srt = YouTubeTranscriptApi.get_transcript(id, languages=['zh-Hans', 'en', 'zh-Hant'])
                print(type(srt))   #srt = list[{}, {},...]
                print(srt)
            except:
                print("There is an error")
                continue


            text_file = open(utils.get_caption_filepath(yt.url), "w", encoding="utf-8")
            text_file.write(json.dumps(srt))

        return data

