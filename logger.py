import datetime

class Logger:
    def __init__(self):
        self.log_file = "/home/overnight-oats/Documents/smart_plotter/log.txt"

    def log(self, log: str):
        msg = str(datetime.datetime.now()) + " | " + str(log)
        print(msg)
        f = open(self.log_file, "a")
        f.write("\n" + msg)
        f.close()