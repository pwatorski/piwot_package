import datetime as dt
from typing import Union

HOURS_IN_DAY = 24
MINUTES_IN_DAY = 1440
SECONDS_IN_DAY = 86400
SECONDS_IN_HOUR = 3600
MINUTES_IN_HOUR = 60
SECONDS_IN_MINUTE = 60
EPOCH_BEGIN = dt.datetime(1970, 1, 2, 1, 0, 0)


def get_timestamp(provided_time:Union[dt.datetime, dt.date, dt.time, dt.timedelta]=None, long:bool=False):
    if not provided_time:
        provided_time = dt.datetime.now()

    if not isinstance(provided_time, dt.datetime) and isinstance(provided_time, dt.date):
        provided_time = dt.datetime(provided_time.year, provided_time.month, provided_time.day)
    if isinstance(provided_time, dt.datetime):
        if EPOCH_BEGIN > provided_time:
            raise AttributeError("Timestamp from datetime cannot be lower than 0!")
        timestamp = provided_time.timestamp()
    elif isinstance(provided_time, dt.timedelta):
        timestamp = provided_time.days * SECONDS_IN_DAY + provided_time.seconds + provided_time.microseconds / 1000000
    else:
        timestamp = provided_time.hour * SECONDS_IN_HOUR + provided_time.minute * SECONDS_IN_MINUTE + provided_time.second + provided_time.microsecond / 1000000

    if long:
        timestamp = int(timestamp * 1000)
    return timestamp

def get_timestamp_simple(long:bool=False):
    timestamp = dt.datetime.now().timestamp()
    if long:
        timestamp = int(timestamp * 1000)
    return timestamp
