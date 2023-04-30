*** Settings ***
Library    ../lib/custom_library.py

*** Variables ***
${username}  pytest_user
${password}  123456

*** Test Cases ***
Verify simple Log In flow
    [Documentation]    Checking log in with correct credentials
    Open browser and navigate to main page
    Click Log In link on Navigation bar
    Log in as User with parameters    ${username}   ${password}
    Assert that user sees welcome label with name    ${username}
    Assert that user sees log out link on the main page
    Close driver


Verify adding highest price product to cart
    [Documentation]    Checking that user is able to add product with highest price to cart
    Open browser and navigate to main page
    Click Log In link on Navigation bar
    Log in as User with parameters    ${username}   ${password}
    Assert that user sees welcome label with name    ${username}
    User clicks Monitor category
    ${product_title}    get highest price product title
    ${product_price}    get highest price product price
    User clicks product by title    ${product_title}
    Assert that user sees product title on the page    ${product_title}
    Assert that user sees product price on the page    ${product_price}
    User clicks add to cart button and close alert on product page
    Click Cart link on navigation bar
    Assert that product with title and price displayed in the cart    ${product_title}  ${product_price}
