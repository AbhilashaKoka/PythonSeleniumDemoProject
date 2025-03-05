Feature: Checking Login Functionality for HR System

  Scenario: Verify login functionality  with valid values
    Given User is on Landing Page
    When User enter username and Passsword
    And Click on Submit
    Then user should able to navigate to next screen

