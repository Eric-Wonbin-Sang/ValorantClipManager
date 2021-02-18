import os

from General import Constants


def reduce_folder_content_to_folder(parent_dir=Constants.ge_valorant_clips_dir):
    """
    This function takes a parent folder with a bunch of folders inside it and takes the contents of each folder and
    moves it into the parent folder.
    """
    for temp_dir in os.listdir(parent_dir):
        if os.path.isdir(parent_dir + "/" + temp_dir):
            print("Dumping {} contents to {}".format(temp_dir, parent_dir))
            for filename in os.listdir(parent_dir + "/" + temp_dir):
                os.rename(
                    parent_dir + "/" + temp_dir + "/" + filename,
                    parent_dir + "/" + filename
                )
                print("\tMoved {} to {}".format(parent_dir + "/" + temp_dir + "/" + filename, parent_dir))
            os.rmdir(parent_dir + "/" + temp_dir)
            print("\t{} deleted".format(temp_dir))
