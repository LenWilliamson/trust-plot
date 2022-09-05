import datetime as dt

def time_converter(time_stamp: float) -> str:
    """
    Accepts posix time stamp in milliseconds and converts it to human readable format
    :param time_stamp: posix time in milliseconds
    :return: %Y-%M-%D %H-%M-%S
    """
    date_time: str = dt.datetime.fromtimestamp(
        time_stamp / 1000).strftime('%Y-%M-%D %H-%M-%S')
    return date_time