import logging
import sys

from internal.settings import config

root = logging.getLogger()
root.setLevel(logging.DEBUG)

ch = logging.StreamHandler(sys.stdout)
fh = logging.FileHandler('../app.log')

if config['logger']['level'].upper() == 'DEBUG':
    lvl = logging.DEBUG
elif config['logger']['level'].upper() == 'WARNING':
    lvl = logging.WARNING
elif config['logger']['level'].upper() == 'ERROR':
    lvl = logging.ERROR
elif config['logger']['level'].upper() == 'CRITICAL':
    lvl = logging.CRITICAL
else:
    lvl = logging.INFO

ch.setLevel(lvl)
fh.setLevel(lvl)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
fh.setFormatter(formatter)
root.addHandler(ch)
root.addHandler(fh)
