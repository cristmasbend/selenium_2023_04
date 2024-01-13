import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService


#  указываем, какой браузер будет запускать: Chrome или Firefox
def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")
    parser.addoption("--drivers_folder", default="/Users/k.zhukovskaia/Documents/selenium_utils")
    parser.addoption("--headless", action="store_true")  # превращает во флаг: true или false


@pytest.fixture(scope="session")
def browser(request):
    browser_name = request.config.getoption("--browser")
    drivers_folder = request.config.getoption("--drivers_folder")
    headless = request.config.getoption("--headless")

    driver = None

    if browser_name == "chrome":
        options = webdriver.ChromeOptions()
        if headless:
            options.add_argument('-headless')
            service = ChromeService(executable_path=os.path.join(f"{drivers_folder}/chromedriver"))
            driver = webdriver.Chrome(service=service, options=options)
    elif browser_name == "firefox":
        options = webdriver.FirefoxOptions()
        options.headless = headless
        driver = webdriver.Firefox(executable_path=os.path.join(f"{drivers_folder}/geckodriver"), options=options)

    driver.maximize_window()

    yield driver

    driver.quit()