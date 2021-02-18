import os

from Classes import Clip, Session
from General import Functions, Constants


def get_clips(clip_dir):
    return [Clip.Clip(clip_dir, filename) for filename in os.listdir(clip_dir)]


def reformat_sessions():
    """
    This function would be used mainly for if the Session max_seconds_between_clips constant was altered.
    """
    Functions.reduce_folder_content_to_folder(parent_dir=Constants.session_parent_dir)
    create_sessions(Constants.session_parent_dir)


def create_sessions(clips_dir):
    clip_list = get_clips(clips_dir)

    if len(clip_list) > 0:
        session_list = Session.divide_clips_to_sessions(
            parent_dir=Constants.session_parent_dir,
            clip_list=clip_list
        )
        for session in session_list:
            print(session)
    else:
        print("There are no clips!")


def main():
    create_sessions(Constants.ge_valorant_clips_dir)


if __name__ == '__main__':
    reformat_sessions()
    # main()
