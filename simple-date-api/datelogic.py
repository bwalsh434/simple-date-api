import datetime
import calendar
import json

from internal.logger import root as app_log


def expand_date(date_obj):
    date_dict = {"full_date": str(date_obj),
                 "date": str(date_obj.date()),
                 "timestamp": str(date_obj.time()),
                 "year": str(date_obj.year),
                 "month": str(date_obj.month),
                 "month_name": str(calendar.month_name[date_obj.month]),
                 "day": str(date_obj.day)
                 }
    return date_dict


def get_date():
    current_date = datetime.datetime.now()
    app_log.log(level=20, msg='Date found!')
    date_dict = expand_date(current_date)
    return json.dumps(date_dict, indent=4)


def get_date_utc():
    current_date_utc = datetime.datetime.utcnow()
    app_log.log(level=20, msg='UTC Date found!')
    date_dict = expand_date(current_date_utc)
    return json.dumps(date_dict, indent=4)

