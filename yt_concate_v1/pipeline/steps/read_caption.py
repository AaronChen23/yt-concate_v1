import os
import json
from pprint import pprint

from yt_concate_v1.settings import CAPTIONS_DIR
from yt_concate_v1.pipeline.steps.step import Step


class ReadCaption(Step):
    def process(self, data, inputs, utils):
        # data = {}
        for yt in data:
            if not utils.caption_file_exists(yt):
                continue

            with open(yt.caption_filepath, "r", encoding="utf-8") as f:       #caption_file=nDysKDELhig.txt
                text = f.read()
                text = json.loads(text)
                print(type(text))
                print(text)

            # data[caption_file] = text
            yt.captions = text
        # pprint(data)
        return data

