import pytest
from selenium.webdriver import Chrome


@pytest.mark.usefixtures("init_driver")
class BaseTest:
    driver: Chrome
    pass
