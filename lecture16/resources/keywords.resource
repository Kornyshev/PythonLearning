*** Settings ***
Documentation     Resource file with custom keywords
Library           ../library/MyLibrary.py

*** Keywords ***
Log In as registered user
    [Arguments]    ${username}   ${password}
    Click Log In link on Navigation Bar
    Log in as User with parameters    ${username}   ${password}
    Assert that user sees Welcome label with name    ${username}
    Assert that user sees Log Out link on the main page