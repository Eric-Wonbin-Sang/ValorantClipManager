import os

from Classes import Clip
from General import Constants


def get_clips(clip_dir):
    return [Clip.Clip(clip_dir, filename) for filename in os.listdir(clip_dir)]


def main():

    clip_list = get_clips(Constants.valorant_clips_dir)
    for clip in clip_list:
        print(clip)


if __name__ == '__main__':
    main()
