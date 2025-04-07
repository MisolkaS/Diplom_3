import pytest
from data.data_browser import *
from helpers import *

@pytest.fixture(params=test_browser)
def fixture_get_driver(request):
    driver = WebdriverFactory.getWebdriver(request.param)

    yield driver

    driver.quit()