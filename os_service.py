import shutil
from os import listdir
import os
from os.path import isfile, join
from logger import Logger
from timer import Timer
from local_constants import FARMER_KEY, PATH_TO_PLOT_COMMAND, PATH_TO_TEMP_DIR, POOL_ADDRESS


class OsService():
    def __init__(self, logger: Logger):
        self.logger = logger
        self.timer = Timer()

    def find_drive_with_space(self, drive_list):
        self.logger.log("searching for a drive with enough space to add a plot...")
        for drive in drive_list:
            if(self.drive_has_space(drive)):
                return drive
            else:
                self.logger.log("moving to next drive")
        self.logger.log("ERROR: NO DRIVE HAS SPACE. Stopping plotting.")
        return ""

    def find_drive_with_og_plots(self, drive_list):
        for drive in drive_list:
            if self.count_files_in_dir(drive + "OG/") > 0:
                return drive

    def drive_has_space(self, drive):
        if(self.get_available_space_on_drive_in_gib(drive) >= 101):
            self.logger.log(drive + " has enough space to add a plot")
            return True
        else:
            self.logger.log(drive + " is full")

    def count_files_in_dir(self, dir: str):
        file_count = len(os.listdir(dir))
        self.logger.log("number of files in " + dir + " is: " + str(file_count))
        return file_count

    def get_available_space_on_drive_in_gib(self, drive: str):
        total, used, free = shutil.disk_usage("D:/")
        gib_available = free // (2**30)
        self.logger.log("GiB available in " + drive + ": " + str(gib_available))
        return gib_available

    def remove_one_file_from_dir(self, dir: str):
        first_file = [f for f in listdir(dir) if isfile(join(dir, f))][0]
        os.remove(dir + "/" + first_file)

    def replace_og_with_pool_plot(self, drive: str):
        self.remove_one_file_from_dir(drive + "OG/")
        self.logger.log("removed one OG plot from " + dir)
        self.plot_to_drive(drive + "Pool/")

    def plot_to_drive(self, drive: str):
        self.clear_ssd()
        self.logger.log("beginning to plot on " + drive + "...")
        self.timer.start_stopwatch()
        os.system(PATH_TO_PLOT_COMMAND + " -n 1 -r 16 -u 512 -t " + PATH_TO_TEMP_DIR + " -d " + drive + " -f " + FARMER_KEY + " -c " + POOL_ADDRESS)
        self.timer.stop_stopwatch()
        self.logger.log("PLOT COMPLETE on " + drive + " - Time taken:" + str(self.timer.get_minutes_elapsed()) + " min")

    def clear_ssd(self):
        file_list = [f for f in listdir(PATH_TO_TEMP_DIR) if isfile(join(PATH_TO_TEMP_DIR, f))]
        for file in file_list:
            os.remove(PATH_TO_TEMP_DIR + "/" + file)
        self.logger.log("cleared SSD")
