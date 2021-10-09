import logging
import os
import time
from configparser import ConfigParser, ExtendedInterpolation

import pkg_resources
import pytest

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


@pytest.hookimpl(hookwrapper=True)
def pytest_fixture_setup(fixturedef, request):
    start = time.time()

    yield

    end = time.time()

    logger.info(
        'pytest_fixture_setup'
        f', request={request}'
        f', time={(end - start) * 1000:8.3f} ms'
    )

@pytest.fixture(scope='session')
def setup_config():
    CONFIG_FN = pkg_resources.resource_filename('example', '../../config/config.ini')
    config = ConfigParser(interpolation=ExtendedInterpolation(), defaults=os.environ)
    config.read(CONFIG_FN)
    return config

@pytest.fixture(scope='session')
def setup_example_fixture_01(setup_config) -> list:
    config = setup_config
    ll = [1, 2]
    return ll

