from time import time
from enum import Enum


# create an enum using the python enum class
class Mode(Enum):
    STANDARD = 1


class Shadow(object):
    def __init__(self):
        self._running = True

        self.update_frequency = 60
        self.mode = Mode.STANDARD


    def loop(self):
        while self._running: 
            current_time = time()


            



            try:
                delta = time.time() - current_time
                time.sleep(1 / self.update_frequency - delta)
            except ValueError:
                pass
