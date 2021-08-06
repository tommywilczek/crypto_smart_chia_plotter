from abc import ABC, abstractmethod
from local_constants import FARMER_KEY, PATH_TO_PLOT_COMMAND, PATH_TO_TEMP_DIR, POOL_ADDRESS
from os import listdir
import os
from os.path import isfile, join
from logger import Logger
from timer import Timer


class OsService(ABC):
    def __init__(self, logger: Logger):
        self.logger = logger
        self.timer = Timer()

    @abstractmethod
    def find_drive_with_space(self, drive_list):
        self.logger.log("searching for a drive with enough space to add a plot...")
        for drive in drive_list:
            if(self.drive_has_space(drive)):
                return drive
            else:
                self.logger.log("moving to next drive")
        self.logger.log("ERROR: NO DRIVE HAS SPACE. Stopping plotting.")
        return ""

    @abstractmethod
    def find_drive_with_og_plots(self, drive_list):
        for drive in drive_list:
            if self.drive_has_space(drive):
                return drive

    @abstractmethod
    def drive_has_space(self, drive):
        if(self.get_available_space_on_drive_in_gb(drive) >= 109):
            self.logger.log(drive + " has enough space to add a plot")
            return True
        else:
            self.logger.log(drive + " is full")

    @abstractmethod
    def count_files_in_dir(self, dir: str):
        file_count = len(os.listdir(dir))
        self.logger.log("number of files in " + dir + " is: " + str(file_count))
        return file_count

    @abstractmethod
    def get_available_space_on_drive_in_gb(self, drive: str):
        pass

    @abstractmethod
    def remove_one_file_from_dir(self, dir: str):
        first_file = [f for f in listdir(dir) if isfile(join(dir, f))][0]
        os.remove(dir + "/" + first_file)
        self.logger.log("removed one OG plot from " + dir)

    @abstractmethod
    def replace_og_with_pool_plot(self, drive: str):
        self.remove_one_file_from_dir(drive)
        self.plot_to_drive(drive)

    @abstractmethod
    def plot_to_drive(self, drive: str):
        self.clear_ssd()
        self.logger.log("beginning to plot on " + drive + "...")
        self.timer.start_stopwatch()
        os.system(PATH_TO_PLOT_COMMAND + " -n 1 -r 16 -u 512 -t " + PATH_TO_TEMP_DIR + " -d " + drive + " -f " + FARMER_KEY + " -c " + POOL_ADDRESS)
        self.timer.stop_stopwatch()
        self.logger.log("PLOT COMPLETE on " + drive + " - Time taken:" + str(self.timer.get_minutes_elapsed()) + " min")

    @abstractmethod
    def clear_ssd(self):
        pass
