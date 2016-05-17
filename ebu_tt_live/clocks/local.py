from datetime import datetime, timedelta
from .base import Clock


class LocalMachineClock(Clock):

    _time_base = 'clock'

    def get_time(self):
        now = datetime.now().time()
        return timedelta(hours=now.hour, minutes=now.minute, seconds=now.second, microseconds=now.microsecond)
