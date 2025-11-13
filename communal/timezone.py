from datetime import datetime

import pendulum

US_EASTERN = pendulum.timezone("US/Eastern")
US_CENTRAL = pendulum.timezone("US/Central")
US_MOUNTAIN = pendulum.timezone("US/Mountain")
US_PACIFIC = pendulum.timezone("US/Pacific")
UTC = pendulum.timezone("UTC")


def local_datetime_utc(*args, **kwargs):
    dt = pendulum.now(*args, **kwargs)
    return datetime.fromtimestamp(dt.timestamp(), UTC)
