from yt_concate_v1.pipeline.steps.step import Step
from moviepy.editor import VideoFileClip, concatenate_videoclips

class EditVideo(Step):
    def process(self, data, inputs, utils):
        clips = []
        for found in data:
            print(found.yt.video_filepath)

            video = VideoFileClip(found.yt.video_filepath).subclip(found.time, found.end_time)
            clips.append(video)
            if len(clips) >= inputs["limit"]:
                break

        final_clip = concatenate_videoclips(clips)
        final_clip.write_videofile(utils.get_output_filepath(inputs["channel_id"], inputs["search_word"]))