import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from data import test_data



@pytest.fixture(scope="session")
def driver():
    url = test_data.login['url']
    driver = webdriver.Chrome()
    driver.get(url)
    driver.maximize_window()
    yield driver
    driver.close()

@pytest.fixture(scope="session", autouse=True)
def authentication(driver):
    login = LoginPage(driver)
    login.enter_login_username(test_data.login['guest']['username'])
    login.enter_login_password(test_data.login['guest']['password'])
    login.click_login_submit_button()


