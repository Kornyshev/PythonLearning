from lecture13.pageobjects.page_factories import User
from lecture13.pageobjects.page_selectors import LoginPageSelectors, InventoryPageSelectors


class LoginPageObject:
    url = "https://www.saucedemo.com/"

    def __init__(self, driver):
        self.driver = driver

    def enter_user_name(self, user_name):
        self.driver.find_element(*LoginPageSelectors.USERNAME_FIELD).send_keys(user_name)

    def enter_password(self, password):
        self.driver.find_element(*LoginPageSelectors.PASSWORD_FIELD).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*LoginPageSelectors.LOGIN_BUTTON).click()

    def login_as_user(self, user: User):
        self.enter_user_name(user.user_name)
        self.enter_password(user.password)
        self.click_login_button()


class InventoryPageObject:
    url = "https://www.saucedemo.com/inventory.html"

    def __init__(self, driver):
        self.driver = driver

    def get_product_cards_titles(self):
        product_cards = self.driver.find_elements(*InventoryPageSelectors.PRODUCT_CARDS_TITLES)
        return [card.text for card in product_cards]
