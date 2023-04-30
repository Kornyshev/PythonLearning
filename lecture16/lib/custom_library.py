from robot.api.deco import keyword
from selenium import webdriver

from lecture16.pageobjects.page_objects import *

driver = webdriver.Chrome()


@keyword
def open_browser_and_navigate_to_main_page():
    driver.maximize_window()
    driver.get(MainPage.url)


@keyword
def close_driver():
    driver.quit()


@keyword
def click_log_in_link_on_navigation_bar():
    NavigationBar(driver).click_log_in_link()


@keyword
def click_cart_link_on_navigation_bar():
    NavigationBar(driver).click_cart_link()


@keyword
def log_in_as_user_with_parameters(username: str, password: str):
    LogInForm(driver).log_in_as_user(User(username, password))


@keyword
def assert_that_user_sees_welcome_label_with_name(username: str):
    assert NavigationBar(driver).get_welcome_label_text() == f'Welcome {username}'


@keyword
def assert_that_user_sees_log_out_link_on_the_main_page():
    assert NavigationBar(driver).is_log_out_link_displayed()


@keyword
def user_clicks_monitor_category():
    MainPage(driver).click_monitors_category()


@keyword
def user_clicks_product_by_title(title: str):
    MainPage(driver).click_product_by_title(title)


@keyword
def get_highest_price_product_title():
    return MainPage(driver).get_product_with_highest_price().title


@keyword
def get_highest_price_product_price():
    return MainPage(driver).get_product_with_highest_price().price


@keyword
def assert_that_user_sees_product_title_on_the_page(title: str):
    assert ProductPage(driver).get_product_title() == title


@keyword
def assert_that_user_sees_product_price_on_the_page(price: str):
    assert price in ProductPage(driver).get_product_price()


@keyword
def user_clicks_add_to_cart_button_and_close_alert_on_product_page():
    product_page = ProductPage(driver)
    product_page.click_add_to_cart()
    product_page.close_alert()


@keyword
def assert_that_product_with_title_and_price_displayed_in_the_cart(title: str, price: str):
    assert any(product == Product(title, price)
               for product in CartPage(driver).get_all_products())
