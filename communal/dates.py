from datetime import date, datetime, timezone

from dateutil.parser import parse as dateutil_parse


def current_timestamp():
    return datetime.now(timezone.utc).timestamp()


def current_year():
    return date.today().year


parse_datetime = dateutil_parse


def parse_date(dt):
    return dateutil_parse(dt).date()


def parse_datetime_ignore_tz_microseconds(d):
    return dateutil_parse(d, ignoretz=True)


def parse_datetime_ignore_tz_seconds(d):
    return dateutil_parse(d, ignoretz=True).replace(microsecond=0)
