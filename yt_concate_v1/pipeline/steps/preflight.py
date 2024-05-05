from yt_concate_v1.pipeline.steps.step import Step

class Preflight(Step):
    def process(self, data, inputs, utils):
        print("in Preflight")
        utils.create_dirs()
