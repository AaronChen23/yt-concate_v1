
class Found:
    def __init__(self, yt, text, time, end_time):
        self.yt = yt
        self.text = text
        self.time = time
        self.end_time = end_time

    def __str__(self):
        return "<Found(yt=" + str(self.yt) + ")>"

    def __repr__(self):
        content = " : ".join([
            "yt=" + str(self.yt),
            "caption=" + str(self.text),
            "time=" + str(self.time)
        ])
        return "<Found(" + content + ")>"
