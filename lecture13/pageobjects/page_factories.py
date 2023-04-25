from seleniumpagefactory.Pagefactory import PageFactory


class User:
    def __init__(self, user_name: str, password: str):
        self.user_name = user_name
        self.password = password


class LoginPage(PageFactory):
    url = "https://www.saucedemo.com/"

    def __init__(self, driver):
        self.driver = driver

    locators = {
        'user_name': ('ID', 'user-name'),
        'password': ('CSS', 'div.form_group #password'),
        'login_button': ('XPATH', '//input[@data-test=\'login-button\']')
    }

    def enter_user_name(self, user_name):
        self.user_name.set_text(user_name)

    def enter_password(self, password):
        self.password.set_text(password)

    def click_login_button(self):
        self.login_button.click()

    def login_as_user(self, user: User):
        self.enter_user_name(user.user_name)
        self.enter_password(user.password)
        self.click_login_button()


class InventoryPage(PageFactory):
    url = "https://www.saucedemo.com/inventory.html"

    def __init__(self, driver):
        self.driver = driver

    locators = {
        'product_cards_titles': ('CSS', 'div.inventory_list > div div.inventory_item_name')
    }

    def get_product_cards_titles(self):
        return self.product_cards_titles.get_text()
