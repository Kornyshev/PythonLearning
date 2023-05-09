from selenium.webdriver.common.by import By


class NavigationSelectors:
    LOG_IN_LINK = (By.CSS_SELECTOR, 'ul.navbar-nav > li > a#login2')
    LOG_OUT_LINK = (By.CSS_SELECTOR, 'ul.navbar-nav > li > a#logout2')
    WELCOME_LABEL = (By.CSS_SELECTOR, 'ul.navbar-nav > li > a#nameofuser')
    SIGN_UP_LINK = (By.CSS_SELECTOR, 'ul.navbar-nav > li > a#signin2')
    CART_LINK = (By.CSS_SELECTOR, 'ul.navbar-nav > li > a#cartur')


class MainPageSelectors:
    PRODUCTS_PRICES = (By.CSS_SELECTOR, 'div#tbodyid div.card-block > h5')
    PRODUCTS_TITLES = (By.CSS_SELECTOR, 'div#tbodyid div.card-block > h4')
    PRODUCTS_TITLE_RELATIVE_TO_PRICE = (By.XPATH, './/../h4')
    MONITORS_CATEGORY = (
        By.XPATH, '//div[@class=\'list-group\']//a[@class=\'list-group-item\' and text()=\'Monitors\']')


class LogInFormSelectors:
    USERNAME_FIELD = (By.CSS_SELECTOR, 'div.form-group input#loginusername')
    PASSWORD_FIELD = (By.CSS_SELECTOR, 'div.form-group input#loginpassword')
    LOGIN_BUTTON = (By.CSS_SELECTOR, 'div.modal-footer button[onclick*=\'logIn\']')


class ProductPageSelectors:
    PRODUCT_TITLE = (By.CSS_SELECTOR, 'div#tbodyid > h2')
    PRODUCT_PRICE = (By.CSS_SELECTOR, 'div#tbodyid > h3')
    ADD_TO_CART = (By.CSS_SELECTOR, 'div#tbodyid a[onclick*=\'addToCart\']')


class CartPageSelectors:
    PRODUCTS = (By.CSS_SELECTOR, 'tbody#tbodyid tr')
