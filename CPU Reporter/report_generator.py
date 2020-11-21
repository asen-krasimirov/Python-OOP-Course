import psutil
import time
from datetime import timedelta, datetime


def measurements_downsample(measurements: list):

    """
    Downsampling the measurements
    """

    return sum(measurements) / len(measurements)


class CPULoad:

    def __init__(self):
        self.collected_load = []
        # self.index = -1

    def get_cpu_load(self, period: 'seconds' = 5):
        start_time = datetime.now()

        self.collected_load.clear()
        loc_measurements = []

        while datetime.now() < start_time + timedelta(seconds=period):
            if len(loc_measurements) >= period:
                self.collected_load.append([datetime.now(), measurements_downsample(loc_measurements)])
                loc_measurements = []
            
            loc_measurements.append(psutil.cpu_percent(interval=0.1))
        return self.collected_load

    # def __iter__(self):
    #     return self

    # def __repr__(self):
    #     return self.collected_load

    # def __next__(self):
        # self.index += 1
        # if self.index >= len(self.collected_load):
        #     raise StopIteration
        # val = self.collected_load[self.index][1]
        # # val = float(val.split('%')[0])
        # return val

    # def __len__(self):
    #     return len(self.collected_load)


if __name__ == "__main__":
    data = CPULoad()
    print(data.get_cpu_load())
    print(len(data))
