import pytest
from selenium import webdriver

from lecture13.pageobjects.page_factories import LoginPage, InventoryPage, User
from lecture13.pageobjects.page_objects import LoginPageObject, InventoryPageObject


@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


# This test method uses PageFactories
def test_single_product_name(driver):
    driver.get(LoginPage.url)
    login_page = LoginPage(driver)
    login_page.login_as_user(User("standard_user", "secret_sauce"))
    inventory_page = InventoryPage(driver)
    assert driver.current_url == InventoryPage.url
    assert inventory_page.get_product_cards_titles() == 'Sauce Labs Backpack'


# This test method uses simple Page Objects (with passing driver inside the PO class)
def test_product_names(driver):
    expected_product_names = [
        'Sauce Labs Backpack', 'Sauce Labs Bike Light', 'Sauce Labs Bolt T-Shirt',
        'Sauce Labs Fleece Jacket', 'Sauce Labs Onesie', 'Test.allTheThings() T-Shirt (Red)'
    ]
    driver.get(LoginPageObject.url)
    login_page = LoginPageObject(driver)
    login_page.login_as_user(User("standard_user", "secret_sauce"))
    inventory_page = InventoryPageObject(driver)
    assert driver.current_url == InventoryPage.url
    assert inventory_page.get_product_cards_titles() == expected_product_names
