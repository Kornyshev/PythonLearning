from lecture14.pageobjects.page_objects import *


def test_simple_log_in(user, driver):
    driver.get(MainPage.url)
    nav_bar = NavigationBar(driver)
    nav_bar.click_log_in_link()
    LogInForm(driver).log_in_as_user(user)
    # expected result: Log out button is presented;  Welcome {username} message is presented
    assert nav_bar.get_welcome_label_text() == f'Welcome {user.username}', \
        f"User can't see welcome label with username {user.username} on the Navigation Bar"
    assert nav_bar.is_log_out_link_displayed(), \
        "User can't see Log Out link on the Navigation Bar"


def test_add_highest_price_product_to_cart(driver):
    main_page = MainPage(driver)
    main_page.click_monitors_category()
    test_product = main_page.get_product_with_highest_price()
    main_page.click_product_by_title(test_product.title)
    product_page = ProductPage(driver)
    # expected result: product's page with {product_name} and {product_price} is open
    assert product_page.get_product_title() == test_product.title, \
        f"User can't see product with title {test_product.title} on the Product page"
    assert test_product.price in product_page.get_product_price(), \
        f"User can't see product with price {test_product.price} on the Product page"
    product_page.click_add_to_cart()
    product_page.close_alert()
    NavigationBar(driver).click_cart_link()
    # expected result: product is successfully added to cart; {product_name} and {product_price} are presented
    assert any(product == test_product for product in CartPage(driver).get_all_products()), \
        f"User can't see product with expected title and price on the Cart page"
