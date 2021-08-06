import subprocess
import os
from os_service import OsService

class LinuxService(OsService):
    def find_drive_with_space(self, drive_list):
        return super().find_drive_with_space(drive_list)

    def find_drive_with_og_plots(self, drive_list):
        return super().find_drive_with_og_plots(drive_list)

    def drive_has_space(self, drive):
        return super().drive_has_space(drive)

    def count_files_in_dir(self, dir: str):
        return super().count_files_in_dir(dir)

    def get_available_space_on_drive_in_gb(self, drive: str):
        df = subprocess.Popen(["df", drive], stdout=subprocess.PIPE)
        output = df.communicate()[0]
        device, size, used, bytes_available, percent, mountpoint = output.split(b"\n")[1].split()
        gb_available = int(bytes_available.decode("utf-8")) / 1000000
        self.logger.log("GB available in " + drive + ": " + str(gb_available))
        return gb_available

    def remove_one_file_from_dir(self, dir: str):
        return super().remove_one_file_from_dir(dir)

    def replace_og_with_pool_plot(self, drive: str):
        return super().replace_og_with_pool_plot(drive)

    def plot_to_drive(self, drive: str):
        return super().plot_to_drive(drive)

    def clear_ssd(self):
        os.system("rm /mnt/ssd/00/*")
        self.logger.log("cleared SSD")