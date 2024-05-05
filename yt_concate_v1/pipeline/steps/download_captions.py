import os
from youtube_transcript_api import YouTubeTranscriptApi


from yt_concate_v1.pipeline.steps.step import Step


class DownloadCaptions(Step):
    def process(self, data, inputs, utils):  #data=video_links
        for url in data:   #url=https://www.youtube.com/watch?v=j8KEkn04n3Y
            print("downloading caption for", url)
            if utils.caption_file_exists(url):
                print("found existing caption file")
                continue
            id = url.split("?v=")[-1]
            try:
                srt = YouTubeTranscriptApi.get_transcript(id, languages=['zh-Hans', 'en', 'zh-Hant'])
                print(srt)
            except:
                print("There is an error")
                continue


            text_file = open(utils.get_caption_filepath(url), "w", encoding="utf-8")
            for i in srt:
                text_file.write("{}\n".format(i))



