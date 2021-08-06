import datetime
from local_constants import LOG_LOCATION

class Logger:
    def __init__(self):
        self.log_file = LOG_LOCATION

    def log(self, log: str):
        msg = str(datetime.datetime.now()) + " | " + str(log)
        print(msg)
        f = open(self.log_file, "a")
        f.write("\n" + msg)
        f.close()