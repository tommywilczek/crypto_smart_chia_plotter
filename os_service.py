from abc import ABC, abstractmethod
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
    def drive_has_space(self, drive):
        if(self.get_available_space_on_drive_in_gb(drive) >= 109):
            self.logger.log(drive + " has enough space to add a plot")
            return True
        else:
            self.logger.log(drive + " is full")

    @abstractmethod
    def count_files_in_dir(self, dir: str):
        pass

    @abstractmethod
    def get_available_space_on_drive_in_gb(self, drive: str):
        pass

    @abstractmethod
    def plot_to_drive(self, drive: str):
        pass

    @abstractmethod
    def clear_ssd(self):
        pass
