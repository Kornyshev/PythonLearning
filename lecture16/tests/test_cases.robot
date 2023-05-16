# robot --outputdir .\lecture16\results .\lecture16\tests\test_cases.robot
# robot --pythonpath C:\Projects\PythonLearning\lecture16\library --listener ScreenshotListener:lecture16\results --outputdir .\lecture16\results .\lecture16\tests\test_cases.robot

*** Settings ***
Library    ../library/MyLibrary.py
Resource   ../resources/keywords.resource
Test Setup    Open Browser and navigate to Main Page
Test Teardown    Close driver

*** Variables ***
${username}  pytest_user
${password}  123456

*** Test Cases ***
Simple Log In test
    [Documentation]    Verify that the user is able to log in
    Click Log In link on Navigation Bar
    Log in as User with parameters    ${username}   ${password}
    Assert that user sees Welcome label with name    ${username}
    Assert that user sees Log Out link on the main page

*** Test Cases ***
Add highest price product from Monitors category to cart
    [Documentation]    Verify that the user is able to add product to cart
    Log In as registered user    ${username}   ${password}
    User clicks Monitor category
    Wait for exact amount of products on the page    2
    ${product_title}    get highest price product title
    ${product_price}    get highest price product price
    User clicks product by title    ${product_title}
    Assert that user sees product title on the page    ${product_title}
    Assert that user sees product price on the page    ${product_price}
    User clicks add to cart button and close alert on product page
    Click Cart link on Navigation Bar
    Assert that product with title and price displayed in the cart    ${product_title}  ${product_price}