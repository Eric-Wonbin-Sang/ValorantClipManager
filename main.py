import os

from Classes import Clip, Session
from General import Constants


def get_clips(clip_dir):
    return [Clip.Clip(clip_dir, filename) for filename in os.listdir(clip_dir)]


def main():

    clip_list = get_clips(Constants.valorant_clips_dir)

    if len(clip_list) > 0:
        session_list = Session.divide_clips_to_sessions(
            parent_dir=Constants.session_parent_dir,
            clip_list=clip_list
        )
        for session in session_list:
            print(session)
    else:
        print("There are no clips!")


if __name__ == '__main__':
    main()
