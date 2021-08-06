import ctypes
from logger import Logger
import os, os.path
from os_service import OsService

class WindowsService(OsService):
    def __init__(self, logger: Logger):
        self.numberParallelPlots = 0
        super().__init__(logger)

    def find_drive_with_space(self, drive_list):
        return super().find_drive_with_space(drive_list)

    def find_drive_with_og_plots(self, drive_list):
        return super().find_drive_with_og_plots(drive_list)

    def drive_has_space(self, drive):
        return super().drive_has_space(drive)

    def count_files_in_dir(self, dir: str):
        return super().count_files_in_dir(dir)

    def get_available_space_on_drive_in_gb(self, drive: str):
        free_bytes = ctypes.c_ulonglong(0)
        ctypes.windll.kernel32.GetDiskFreeSpaceExW(ctypes.c_wchar_p(drive), None, None, ctypes.pointer(free_bytes))
        bytes_in_one_gb = 1000000000
        return free_bytes.value / bytes_in_one_gb

    def remove_one_file_from_dir(self, dir: str):
        return super().remove_one_file_from_dir(dir)

    def replace_og_with_pool_plot(self, drive: str):
        return super().replace_og_with_pool_plot(drive)

    def plot_to_drive(self, drive: str):
        return super().plot_to_drive(drive)

    def clear_ssd(self):
        os.system("del /q E:\\TempPlots\\*")
