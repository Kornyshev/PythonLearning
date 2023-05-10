import configparser

import pytest
from selenium import webdriver

from lecture14.pageobjects.page_objects import *


@pytest.fixture(scope="session")
def user():
    config = configparser.ConfigParser()
    config.read('properties/user.ini')
    return User(config.get('User', 'username'), config.get('User', 'password'))


@pytest.fixture(scope="session")
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def login(user, driver):
    driver.get(MainPage.url)
    NavigationBar(driver).click_log_in_link()
    LogInForm(driver).log_in_as_user(user)
    assert NavigationBar(driver).get_welcome_label_text() == f'Welcome {user.username}'


@pytest.fixture(scope="function")
def logout(user, driver):
    yield
    NavigationBar(driver).click_log_out_link()
