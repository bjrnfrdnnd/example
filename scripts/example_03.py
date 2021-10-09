import logging
import os
import pathlib
import string
import sys
from configparser import ConfigParser, ExtendedInterpolation

import pandas as pd
import numpy as np
import pkg_resources

from example.example import print_hi, setup_logging, setup_pandas_printing

logger = logging.getLogger(__name__)

EXAMPLE_DATA_FILE_NAME = pkg_resources.resource_filename('example', '../../data/example_data.txt')
CONFIG_FN = pkg_resources.resource_filename('example', '../../config/config.ini')
LOGGING_FN = pkg_resources.resource_filename('example', '../../config/logging.ini')

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
    setup_logging(logging_fn=LOGGING_FN)

    setup_pandas_printing()
    size_ = 24
    df = pd.DataFrame(data=np.random.random((size_, size_)), columns=list(string.ascii_uppercase)[:size_])
    print(df)

    logger.info('df')



if __name__ == '__main__':
    sys.exit(main(sys.argv))