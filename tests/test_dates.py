from datetime import date, datetime

from communal.dates import (
    current_timestamp,
    current_year,
    parse_date,
    parse_datetime,
    parse_datetime_ignore_tz_microseconds,
    parse_datetime_ignore_tz_seconds,
)


def test_current_timestamp():
    ts = current_timestamp()
    assert isinstance(ts, float)
    assert ts > 0


def test_current_year():
    year = current_year()
    assert isinstance(year, int)
    assert year >= 2020  # Reasonable check


def test_parse_datetime():
    dt = parse_datetime("2023-01-15 10:30:00")
    assert isinstance(dt, datetime)
    assert dt.year == 2023
    assert dt.month == 1
    assert dt.day == 15

    dt2 = parse_datetime("2023-01-15T10:30:00")
    assert isinstance(dt2, datetime)


def test_parse_date():
    d = parse_date("2023-01-15")
    assert isinstance(d, date)
    assert d.year == 2023
    assert d.month == 1
    assert d.day == 15

    d2 = parse_date("2023-01-15 10:30:00")
    assert isinstance(d2, date)


def test_parse_datetime_ignore_tz_microseconds():
    dt = parse_datetime_ignore_tz_microseconds("2023-01-15T10:30:00+05:00")
    assert isinstance(dt, datetime)
    assert dt.tzinfo is None


def test_parse_datetime_ignore_tz_seconds():
    dt = parse_datetime_ignore_tz_seconds("2023-01-15T10:30:00.123456+05:00")
    assert isinstance(dt, datetime)
    assert dt.tzinfo is None
    assert dt.microsecond == 0
