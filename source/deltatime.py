
import time
class deltatime:

    def __init__(self):

        self.ptime = time.time()
        self.ntime = None
        self.dt = None

    def update(self):
        self.ntime = time.time()
        self.dt =  self.ntime - self.ptime
        self.dt *= 60
        self.ptime = self.ntime
