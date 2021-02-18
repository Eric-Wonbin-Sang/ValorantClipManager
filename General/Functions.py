import os

from General import Constants


def reduce_folder_content_to_folder(parent_dir=Constants.valorant_clips_dir):
    """
    This function takes a parent folder with a bunch of folders inside it and takes the contents of each folder and
    moves it into the parent folder.
    """
    for temp_dir in os.listdir(parent_dir):
        print(temp_dir)
        for filename in os.listdir(parent_dir + "/" + temp_dir):
            print("\t", filename)
            os.rename(
                parent_dir + "/" + temp_dir + "/" + filename,
                parent_dir + "/" + filename
            )
        os.rmdir(parent_dir + "/" + temp_dir)
