# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import logging
import logging.config
import pandas as pd


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

def setup_logging(logging_fn: str = None):
    # set up logging
    logging.config.fileConfig(logging_fn, disable_existing_loggers=False)

def setup_pandas_printing():
    # set pandas print options
    pd.set_option('display.width', 300)
    pd.set_option('display.max_columns', 300)
    pd.set_option('mode.chained_assignment', 'raise')