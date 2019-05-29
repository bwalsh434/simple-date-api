import datetime

import datelogic


def test_expand_date_month():
    current_date = datetime.datetime.now()
    date_dict = datelogic.expand_date(current_date)
    assert str(datetime.datetime.now().month) == date_dict["month"]


def test_get_date_timestamp_exists():
    assert "timestamp" in datelogic.get_date()


def test_get_date_utc_timestamp_exists():
    assert "timestamp" in datelogic.get_date_utc()
