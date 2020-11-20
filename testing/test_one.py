import psutil
import time
from datetime import timedelta, datetime


def get_cpu_load(period: 'seconds' = 10, start_time=datetime.now()):

    collected_load = []
    while datetime.now() < start_time + timedelta(seconds=period):
        # current_time = datetime.strftime(datetime.now(), "%H:%M:%S:%f")
        current_measurement = psutil.cpu_percent()
        if current_measurement != 0.0:
            collected_load.append((datetime.now(), current_measurement))
        time.sleep(0.001)

    return collected_load


data = get_cpu_load(10)
print(data)
print(len(data))
