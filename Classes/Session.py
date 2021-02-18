
class Session:

    def __init__(self, clip_list):

        self.clip_list = clip_list


def divide_clips_to_sessions(clip_list, max_seconds_between_clips=60 * 60 * 4):
    prev_clip = None
    temp_clip_list_list = []
    temp_clip_list = []
    for curr_clip in clip_list:
        temp_clip_list.append(curr_clip)
        if prev_clip is not None:
            if (curr_clip.dt - prev_clip.dt).total_seconds() > max_seconds_between_clips:
                temp_clip_list_list.append(temp_clip_list)
                temp_clip_list = []
        prev_clip = curr_clip
    temp_clip_list_list.append(temp_clip_list)

    print("Clip separation",
          "successful" if len(clip_list) == sum(len(c_list) for c_list in temp_clip_list_list) else "unsuccessful")

    return [Session(clip_list) for clip_list in temp_clip_list_list if clip_list]
