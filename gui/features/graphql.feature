# Created by oscar.valerio at 9/29/21
# https://behave.readthedocs.io/en/latest/api.html#model-objects
# https://behave.readthedocs.io/en/latest/tag_expressions.html#tag-expressions-v2
# https://behave.readthedocs.io/en/latest/more_info.html#

@graphql
Feature: Tests to validate graphql functionality
  In this feature file we are covering all possible tests related to graphql

  @wip
  Scenario: Get all products query
    When I send query with name PRODUCTS
    Then The status code should be 200
    And The response json should have these keys
      | expected_key                      |
      | products.edges[*].node.id         |
      | products.edges[*].node.name       |
      | products.edges[*].node.type       |
      | products.edges[*].node.totalSales |
    And Each products.edges[*].node.id into json node products should have a string value
    And Each products.edges[*].node.name into json node products should have a string value
    And Each products.edges[*].node.type into json node products should have a string value
    And Each products.edges[*].node.totalSales into json node products should have a string value
    And The response time should be less than 1500 ms

