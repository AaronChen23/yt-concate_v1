from yt_concate_v1.pipeline.steps.step import Step
from yt_concate_v1.model.yt import YT


class InitializeYT(Step):
    def process(self, data, inputs, utils):  #data=video_links
        # for url in data:
        #     return YT(url)
        return [YT(url) for url in data]   #注意:寫成上述程式碼YT(url)不會有literable(但是為什麼還不知道)

