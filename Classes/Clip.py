import datetime


class Clip:

    def __init__(self, parent_dir, filename):

        self.parent_dir = parent_dir
        self.filename = filename

        self.dt = self.get_dt()

    def get_dt(self):
        temp_str = " ".join(self.filename.split(" ")[1:])
        temp_str = ".".join(temp_str.split(".")[:-2])
        return datetime.datetime.strptime(temp_str, "%Y.%m.%d - %H.%M.%S.%f")

    def __str__(self):
        return "Clip - {}".format(
            self.dt
        )
