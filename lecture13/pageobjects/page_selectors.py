from selenium.webdriver.common.by import By


class LoginPageSelectors:
    USERNAME_FIELD = (By.ID, 'user-name')
    PASSWORD_FIELD = (By.CSS_SELECTOR, 'div.form_group #password')
    LOGIN_BUTTON = (By.XPATH, '//input[@data-test=\'login-button\']')


class InventoryPageSelectors:
    PRODUCT_CARDS_TITLES = (By.CSS_SELECTOR, 'div.inventory_list > div div.inventory_item_name')
