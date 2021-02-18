import os
import time
import datetime

from Classes import Clip, Session
from General import Functions, Constants


def get_clips(clip_dir):
    return [Clip.Clip(clip_dir, filename) for filename in os.listdir(clip_dir)]


def reformat_sessions(sessions_parent_dir):
    """
    This function would be used mainly for if the Session max_seconds_between_clips constant was altered.
    """
    Functions.reduce_folder_content_to_folder(parent_dir=sessions_parent_dir)
    create_sessions(sessions_parent_dir)


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


def listen_for_clips(clips_dir, sessions_parent_dir):

    while True:
        print(datetime.datetime.now(), end=" - ")
        clip_list = get_clips(clips_dir)
        if len(clip_list) != 0:
            session_dir_list = os.listdir(sessions_parent_dir)
            session_dir = session_dir_list[-1] if session_dir_list else None
            if session_dir:
                for filename in os.listdir(sessions_parent_dir + "/" + session_dir):
                    os.rename(sessions_parent_dir + "/" + session_dir + "/" + filename, clips_dir + "/" + filename)
            create_sessions(clips_dir)
        else:
            print("No clips")
        time.sleep(5)


def main():
    # reformat_sessions(sessions_parent_dir=Constants.session_parent_dir)
    # create_sessions(Constants.ge_valorant_clips_dir)

    listen_for_clips(
        clips_dir=Constants.ge_valorant_clips_dir,
        sessions_parent_dir=Constants.session_parent_dir
    )


if __name__ == '__main__':
    main()
