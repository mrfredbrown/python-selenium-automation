# Created by Fred at 1/3/2021
Feature: Verify user can add item to cart on Amazon
  # This is a testcase to verify cart on Amazon
  Scenario: User can verify added item in cart
    Given Open Amazon homepage
    When User types watches and submits
    When User adds watch to cart
    Then User verifies watch in cart



#    And User clicks on cart
#    Then Verify cart