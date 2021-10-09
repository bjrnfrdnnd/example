import pandas as pd
import numpy as np
import pytest

@pytest.fixture(scope="class", autouse=True)
def setup_00():
    print("setup_00 00")
    yield
    print("teardown")



class TestExample:
    # @pytest.mark.run_these_please
    # @pytest.mark.asyncio
    def test_example(self, setup_example_fixture_01):
        ll = setup_example_fixture_01
        print(ll)
        assert True
