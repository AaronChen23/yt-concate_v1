from yt_concate_v1.pipeline.steps.step import Step
from yt_concate_v1.model.found import Found
class Search(Step):
    def process(self, data, inputs, utils):
        search_word = inputs["search_word"]

        found = []
        for yt in data:
            captions = yt.captions   #captions=[{:}, {:}, {:}...]

            if not captions:
                continue

            for caption in captions:
                if search_word in caption["text"]:
                    text = caption["text"]
                    time = caption["start"]
                    f = Found(yt, text, time)
                    found.append(f)  #因為append只能每次append一個東西
        print(found)
        print(len(found))
        return found
