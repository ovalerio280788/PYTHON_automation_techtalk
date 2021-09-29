# Created by oscar.valerio at 9/28/21
# https://behave.readthedocs.io/en/latest/api.html#model-objects
# https://behave.readthedocs.io/en/latest/tag_expressions.html#tag-expressions-v2
# https://behave.readthedocs.io/en/latest/more_info.html#

@login
Feature: Tests to validate the login page functionality
  In this feature file we are covering all possible tests related to the login page

  @negative_test
  Scenario Outline: Login with Invalid credentials
    When I visit the login page
    And I fill the username field with value <username>
    And I fill the password field with value <password>
    And I click on Log In button
    Then I should see an error message with text <expected_error>

    Examples:
      | username | password | expected_error                                           |
      # empty username and password
      |          |          | Error: Username is required.                             |
      # valid username / invalid password
      | auto     |          | Error: The password field is empty.                      |
      # invalid username / invalid password
      | invalid  | invalid  | Unknown username. Check again or try your email address. |


  Scenario: Login with valid credentials
    When I log in with valid credentials
    Then I should see the login message "Hello auto (not auto? Log out)"
    And I should not see the username and password fields