import datetime
import os
import time

import pytest
from appium import webdriver as appium_driver
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from congenica_test.capabilities import Capabilities
from congenica_test.logger import get_logger
from congenica_test.src.helpers.android.android_authorization import android_authorization
from congenica_test.src.helpers.ios.ios_authorization import ios_authorization

logger = get_logger()


def android_device_name() -> str:
    if os.getenv('PYTEST_XDIST_WORKER') == 'gw0':
        return 'emulator-5554'
    elif os.getenv('PYTEST_XDIST_WORKER') == 'gw1':
        return 'emulator-5556'
    else:
        return 'emulator-5554'


@pytest.hookimpl
def pytest_addoption(parser):
    parser.addoption('--app', action='store', default="ios", help="Choose App: ios or android")
    parser.addoption('--device', action='store', default="emulator", help="Choose Device: simulator / emulator / real "
                                                                          "device / bs")

@pytest.fixture(scope="session")
def app(request):
    return request.config.getoption("--app")


@pytest.fixture(scope="session")
def device(request):
    return request.config.getoption("--device")


def driver_setup(app: str, device: str):
    logger.info("Driver session setup")
    logger.info("Configuring desired capabilities")
    capabilities = Capabilities()
    logger.info("Initiating driver")

    if app == "web":
        options = webdriver.ChromeOptions()
        options.add_argument('--no-sandbox')
        options.add_argument('--remote-debugging-port=9222')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        options.add_argument('--profile-directory=Default')
        return webdriver.Chrome(ChromeDriverManager().install(), options=options)
    desired_caps = capabilities.get_capabilities(device=device, app=app)
    driver = appium_driver.Remote(command_executor=capabilities.CURRENT_EXECUTOR,
                                  desired_capabilities=desired_caps)

    logger.info("Driver setup success")
    return driver


@pytest.fixture(scope='session', autouse=True)
def driver(request, app, device):
    driver = driver_setup(app=app, device=device)
    yield driver
    status_str = "failed" if request.node.testsfailed else "passed"
    if device == 'bs':
        driver.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": '
            '{"status":"' + status_str + '", "reason":"Reason"}}'
        )
    logger.info("driver quit")
    driver.quit()


@pytest.fixture(autouse=True, scope="session")
def authorization(driver, app):
    if app == "ios":
        ios_authorization(driver)
    elif app == "android":
        android_authorization(driver)
    elif app == "web":
        pass


@pytest.fixture(autouse=True, scope="function")
def screenshot(request, driver):
    yield
    if request.node.report.failed:
        driver.save_screenshot(
            f"screenshots/{request.node.name}_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.png")


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    item.report = outcome.get_result()
