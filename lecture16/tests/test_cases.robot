# robot --outputdir .\lecture16\results .\lecture16\tests\test_cases.robot

*** Settings ***
Library    C:/Projects/PythonLearning/lecture16/library/MyLibrary.py
Resource   C:/Projects/PythonLearning/lecture16/resources/keywords.resource

*** Variables ***
${username}  pytest_user
${password}  123456

*** Test Cases ***
Simple Log In test
    [Documentation]    Verify that the user is able to log in
    [Setup]    Open Browser and navigate to Main Page
    Click Log In link on Navigation Bar
    Log in as User with parameters    ${username}   ${password}
    Assert that user sees Welcome label with name    ${username}
    Assert that user sees Log Out link on the main page
    [Teardown]    Close driver

*** Test Cases ***
Add highest price product from Monitors category to cart
    [Documentation]    Verify that the user is able to add product to cart
    [Setup]    Open Browser and navigate to Main Page
    Log In as registered user    ${username}   ${password}
    User clicks Monitor category
    ${product_title}    get highest price product title
    ${product_price}    get highest price product price
    User clicks product by title    ${product_title}
    Assert that user sees product title on the page    ${product_title}
    Assert that user sees product price on the page    ${product_price}
    User clicks add to cart button and close alert on product page
    Click Cart link on Navigation Bar
    Assert that product with title and price displayed in the cart    ${product_title}  ${product_price}
    [Teardown]    Close driver
