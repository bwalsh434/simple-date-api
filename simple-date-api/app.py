from flask import Flask

from internal.logger import root as app_log
from internal.settings import config
from datelogic import get_date, get_date_utc

app = Flask(__name__)


@app.route("/")
def index_endpoint():
    return "You've reached the index! Date API v2"


@app.route("/date")
def date_endpoint():
    if config['date_settings']['timezone'] == 'utc':
        date_json = get_date_utc()
    else:
        date_json = get_date()
    return date_json


if __name__ == "__main__":
    app_log.log(level=20, msg='Starting simple-date-api application')
    app.run(host='0.0.0.0')
