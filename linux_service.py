import subprocess
import os
from os_service import OsService

class LinuxService(OsService):
    def find_drive_with_space(self, drive_list):
        return super().find_drive_with_space(drive_list)

    def drive_has_space(self, drive):
        return super().drive_has_space(drive)

    def count_files_in_dir(self, dir: str):
        file_count = len(os.listdir(dir))
        self.logger.log("number of files in " + dir + " is: " + file_count)
        return file_count

    def get_available_space_on_drive_in_gb(self, drive: str):
        df = subprocess.Popen(["df", drive], stdout=subprocess.PIPE)
        output = df.communicate()[0]
        device, size, used, bytes_available, percent, mountpoint = output.split(b"\n")[1].split()
        gb_available = int(bytes_available.decode("utf-8")) / 1000000
        self.logger.log("GB available in " + drive + ": " + str(gb_available))
        return gb_available
        
    def plot_to_drive(self, drive: str):
        self.clear_ssd()
        self.logger.log("beginning to plot on " + drive + "...")
        self.timer.start_stopwatch()
        os.system("/home/overnight-oats/chia-plotter/build/chia_plot -n 1 -r 16 -u 512 -t /mnt/ssd/00/ -d " +
            drive +
            " -f a180dff519ede12eab4af47bc8b05fb3ad25e779df0ba142ed20b5ca857fbb9c7e9546218331b7bf7a9308074318366a " +
            "-c xch124q8d2708vhkfjp3qkta5gdq3vuwa2au6m0atlurpat7fxv3ksuq3tu4nh")
        self.timer.stop_stopwatch()
        self.logger.log("PLOT COMPLETE on " + drive + " - Time taken:" + str(self.timer.get_minutes_elapsed()) + " min")

    def clear_ssd(self):
        os.system("rm /mnt/ssd/00/*")
        self.logger.log("cleared SSD")