import os

from Classes import Clip, Session
from General import Constants


def get_clips(clip_dir):
    return [Clip.Clip(clip_dir, filename) for filename in os.listdir(clip_dir)]


def main():

    clip_list = get_clips(Constants.valorant_clips_dir)
    # for clip in clip_list:
    #     print(clip)

    session_list = Session.divide_clips_to_sessions(clip_list)
    # for session in session_list:
    #     print(session)


if __name__ == '__main__':
    main()
