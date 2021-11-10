import logging
import os
import pathlib
import string
import sys
from configparser import ConfigParser, ExtendedInterpolation

import importlib_resources
import pandas as pd
import numpy as np
import pkg_resources

import example
from example.example import print_hi, setup_logging, setup_pandas_printing

logger = logging.getLogger(__name__)

BASE_DIR: pathlib.Path = importlib_resources.files(example) # this is a traversable. As this is not a zip file, but an actual path, this works
DATA_DIR = BASE_DIR.parent.parent / 'data'
CONFIG_DIR = BASE_DIR.parent.parent / 'config'
CONFIG_FN = CONFIG_DIR / 'config.ini'
LOGGING_FN = CONFIG_DIR / 'logging.ini'
EXAMPLE_DATA_FILE_NAME = DATA_DIR / 'example_data.txt'


def main(argv):
    print_hi('example')
    print(EXAMPLE_DATA_FILE_NAME)
    a = pkg_resources.resource_stream('example', '../../data/example_data.txt')
    b = a.readline()
    print(b)
    c = pathlib.Path(EXAMPLE_DATA_FILE_NAME)
    d = c.is_file()
    print(d)
    e = c.read_text()
    print(e)

    # load the config file
    config = ConfigParser(interpolation=ExtendedInterpolation(), defaults=os.environ)
    config.read(CONFIG_FN)

    db_username = config.get('DataBase', 'db_username')
    print(db_username)

    print(LOGGING_FN)
    setup_logging(logging_fn=LOGGING_FN.resolve().__str__())

    setup_pandas_printing()
    size_ = 24
    df = pd.DataFrame(data=np.random.random((size_, size_)), columns=list(string.ascii_uppercase)[:size_])
    print(df)

    logger.info('df')



if __name__ == '__main__':
    sys.exit(main(sys.argv))