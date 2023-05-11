from typing import List

from custom_selectors.my_selectors import *
from models.product import Product
from models.user import User
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class MainPage:
    url = "https://www.demoblaze.com/"

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def click_product_by_title(self, title):
        product_titles = self.driver.find_elements(*MainPageSelectors.PRODUCTS_TITLES)
        matching_titles = [pt for pt in product_titles if pt.text == title]
        if matching_titles:
            matching_titles[0].click()
        else:
            raise NoSuchElementException(f'Element with title {title} was not found')

    def click_monitors_category(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(MainPageSelectors.MONITORS_CATEGORY)).click()

    def get_product_with_highest_price(self) -> Product:
        # Necessary waiting, because there is nothing on the page to bind to when switching between categories
        # time.sleep(3)
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(MainPageSelectors.PRODUCTS_PRICES))
        elements = self.driver.find_elements(*MainPageSelectors.PRODUCTS_PRICES)
        element = max(elements, key=lambda x: int(x.text.strip('$')))
        return Product(element.find_element(*MainPageSelectors.PRODUCTS_TITLE_RELATIVE_TO_PRICE).text, element.text)

    def wait_for_exact_amount_of_elements(self, amount: int):
        WebDriverWait(self.driver, 10).until(
            lambda driver: len(driver.find_elements(*MainPageSelectors.PRODUCTS_PRICES)) == amount,
            f"Expected {amount} price elements, "
            f"but found {len(self.driver.find_elements(*MainPageSelectors.PRODUCTS_PRICES))}")


class LogInForm:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def type_username(self, username):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(LogInFormSelectors.USERNAME_FIELD)).send_keys(username)

    def type_password(self, password):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(LogInFormSelectors.PASSWORD_FIELD)).send_keys(password)

    def click_log_in_button(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(LogInFormSelectors.LOGIN_BUTTON)).click()

    def log_in_as_user(self, user: User):
        self.type_username(user.username)
        self.type_password(user.password)
        self.click_log_in_button()


class ProductPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def close_alert(self):
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        self.driver.switch_to.alert.dismiss()

    def click_add_to_cart(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(ProductPageSelectors.ADD_TO_CART)).click()

    def get_product_title(self) -> str:
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(ProductPageSelectors.PRODUCT_TITLE)).text

    def get_product_price(self) -> str:
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(ProductPageSelectors.PRODUCT_PRICE)).text


class CartPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def get_all_products(self) -> List[Product]:
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(CartPageSelectors.PRODUCTS))
        return [Product(elem.find_element(By.XPATH, './td[2]').text, '$' + elem.find_element(By.XPATH, './td[3]').text)
                for elem in self.driver.find_elements(*CartPageSelectors.PRODUCTS)]


class NavigationBar:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def click_log_in_link(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(NavigationSelectors.LOG_IN_LINK)).click()

    def click_log_out_link(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(NavigationSelectors.LOG_OUT_LINK)).click()
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(NavigationSelectors.LOG_IN_LINK))

    def click_cart_link(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(NavigationSelectors.CART_LINK)).click()

    def is_log_out_link_displayed(self) -> bool:
        return self.driver.find_element(*NavigationSelectors.LOG_OUT_LINK).is_displayed()

    def get_welcome_label_text(self) -> str:
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(NavigationSelectors.WELCOME_LABEL)).text
