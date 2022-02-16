import allure
import pytest
from selenium import webdriver
from Utilities.ConfigReader import get_property


@pytest.fixture(params=[get_property("browser")], scope='function')
def init_driver(request):
    global web_driver
    if request.param == "chrome":
        web_driver = webdriver.Chrome()
    if request.param == "firefox":
        web_driver = webdriver.Firefox()
    request.cls.driver = web_driver
    web_driver.get(get_property("url"))
    web_driver.implicitly_wait(10)
    web_driver.maximize_window()
    yield
    web_driver.quit()


"""
browser method is used to pass the browser from command line
"""


def browser(request):
    return request.config.getoption("--browser")


"""
pytest_addoption method is used to pass the browser from command line
"""


def pytest_addoption(parser):
    parser.addoption("--browser",
                     dest="browser",
                     action="store",
                     default='Chrome',
                     help="Browser. Valid options are chrome and firefox")


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])
    if report.when == "call":
        # always add url to report
        #extra.append(pytest_html.extras.url("http://www.example.com/"))
        #report.extra = extra
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            # only add additional html on failure
            allure.attach(
                web_driver.get_screenshot_as_png(),
                name='screenshot',
                attachment_type=allure.attachment_type.PNG)

