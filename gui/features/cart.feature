# Created by oscar.valerio at 9/28/21
# https://behave.readthedocs.io/en/latest/api.html#model-objects
# https://behave.readthedocs.io/en/latest/tag_expressions.html#tag-expressions-v2
# https://behave.readthedocs.io/en/latest/more_info.html#

@cart
Feature: Tests to validate the cart page functionality
  In this feature file we are covering all possible tests related to the cart page

  Background:
    Given I log in with valid credentials

  @clear_cart
  Scenario: Verify user can add a product to the cart.
    When I add product to the cart with parameters
      | Name   | Color | Logo | Items |
      | Hoodie | Blue  | Yes  | 3     |
    And I visit the cart page
    Then I should see this product added in the table
      | Product            | Quantity | Price | Subtotal |
      | Hoodie - Blue, Yes | 3        | n/a   | n/a      |


  @clear_cart @retry_2
  Scenario: Verify user can add multiple products to the cart.
    When I add products to the cart with parameters
      | Name   | Color | Logo | Items |
      | Hoodie | Blue  | Yes  | 3     |
      | Hoodie | Green | No   | 2     |
    And I visit the cart page
    Then I should see this product added in the table
      | Product            | Quantity | Price | Subtotal |
      | Hoodie - Blue, Yes | 3        | n/a   | n/a      |
      | Hoodie - Green, No | 2        | n/a   | n/a      |
