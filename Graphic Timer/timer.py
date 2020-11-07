from datetime import timedelta
import pyfiglet


class Timer:

    def __init__(self, hours: int, minutes: int, seconds: int):
        self.__time = timedelta(hours=hours, minutes=minutes, seconds=seconds)

    @classmethod
    def from_string(cls, time: str) -> 'Timer':
        hours, minutes, seconds = [int(elem) for elem in time.split('.')]
        return cls(hours, minutes, seconds)

    @classmethod
    def from_minutes(cls, minutes) -> 'Timer':
        hours, minutes, seconds = 0, minutes, 0
        if minutes >= 60:
            hours = minutes // 60
            minutes = minutes % 60

        return cls(hours, minutes, seconds)

    @property
    def time(self):
        hours, minutes, seconds = str(self.__time).split(':')
        result = f"{hours.zfill(2)}:{minutes.zfill(2)}:{seconds.zfill(2)}"
        result = pyfiglet.figlet_format(result, font="doh")

        return result

    def pass_one_second(self):
        self.__time = self.__time - timedelta(seconds=1)
        return self.time

    def is_finished(self):
        if self.time == pyfiglet.figlet_format("00:00:00", font="doh"):
            return True
        return False
