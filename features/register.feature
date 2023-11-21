Feature: Registration Functionality
  @registration_with_mandatory
  Scenario: Registration with mandatory fields
    Given I navigate to register page
    When I enter mandatory fields
    And I Select Privacy Policy
    And I click on Register button
    Then Account should be created

  @register_with_all_fields
  Scenario: Registration with all fields
    Given I navigate to register page
    When I enter all fields
    And I click on Register button
    Then Account should be created

  @register_with_existing_email
  Scenario: Register with a duplicate email address
    Given I navigate to register page
    When I enter all fields except email field
    And I enter existing email address on email field
    And I Select Privacy Policy
    And I click on Register button
    Then I should get proper warning message

  @register_without_providing_data
  Scenario: Register without providing any fields
    Given I navigate to register page
    When I dont enter anything into fields
    And I click on Register button
    Then I should get Proper warning message every mandatory fields should be displayed

  @register_without_data_only_click_policy
  Scenario: Register without providing any fields but only click policy
    Given I navigate to register page
    When I dont enter anything into fields
    And I click on Policy check box
    And I click on Register button
    Then I should get Proper warning message are you an existing user
