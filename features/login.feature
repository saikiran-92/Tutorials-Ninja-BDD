Feature: Login Functionality
  @login_completed
  Scenario: Login with valid credentials
    Given I got navigate to login page
    When I enter valid email id and valid password into the fields
    And I click on login button
    Then I should logged in

  @login_with_invalid_email
  Scenario: Login with invalid email id and valid password
    Given I got navigated to login page
    When I enter invalid email id and valid password into the fields
    And I click on login button
    Then I should get Proper warning message Invalid Email id

  @login_with_invalid_password
  Scenario: Login with valid email id and invalid password
    Given I got navigated to login page
    When I enter valid email id and invalid password into fields
    And I click on login button
    Then I should get proper warning message Invalid Password

  @login_without_credentials
  Scenario: Login without email id and password
    Given I got navigated to login page
    When I not enter email id and password into fields
    And I click on login button
    Then I should get proper warning message Enter Email id and Password