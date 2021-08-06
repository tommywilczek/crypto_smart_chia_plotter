import time

class Timer:
    def __init__(self):
        self.__start_time = 0
        self.__end_time = 0

    def start_stopwatch(self):
        self.__start_time = time.time()

    def stop_stopwatch(self):
        self.__end_time = time.time()

    def get_minutes_elapsed(self):
        return round((self.__end_time - self.__start_time) / 60, 2)