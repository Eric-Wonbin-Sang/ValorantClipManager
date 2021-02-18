import os

from General import Constants


class Session:

    max_seconds_between_clips = Constants.session_max_seconds_between_clips

    def __init__(self, parent_dir, clip_list):

        self.parent_dir = parent_dir
        self.clip_list = clip_list
        self.session_name = self.get_session_name()
        self.session_dir = self.parent_dir + "/" + self.session_name

        self.create_dir()
        self.move_clips()

    def get_session_name(self):
        return "Session " + self.clip_list[0].dt.strftime("%Y.%m.%d - %H.%M.%S")

    def create_dir(self):
        if not os.path.isdir(self.session_dir):
            os.mkdir(self.session_dir)
            print(self.session_dir, "created")
        else:
            print(self.session_dir, "already exists!")

    def move_clips(self):
        for clip in self.clip_list:
            os.rename(clip.parent_dir + "/" + clip.filename, self.session_dir + "/" + clip.filename)

    def __str__(self):
        return "{}: contains {} clips".format(
            self.session_name,
            len(self.clip_list)
        )


def divide_clips_to_sessions(parent_dir, clip_list):

    print("Clip separation... ", end="")

    prev_clip = None
    temp_clip_list_list = []
    temp_clip_list = []
    for curr_clip in clip_list:
        temp_clip_list.append(curr_clip)
        if prev_clip is not None:
            if (curr_clip.dt - prev_clip.dt).total_seconds() > Session.max_seconds_between_clips:
                temp_clip_list_list.append(temp_clip_list)
                temp_clip_list = []
        prev_clip = curr_clip
    temp_clip_list_list.append(temp_clip_list)

    if len(clip_list) == sum(len(c_list) for c_list in temp_clip_list_list):
        print("successful!")
    else:
        print("unsuccessful! Clip length and clip list lengths in all sessions do not match!")

    return [Session(parent_dir, clip_list) for clip_list in temp_clip_list_list if clip_list]
