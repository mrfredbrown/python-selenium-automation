# Created by Fred at 12/24/2021
# Created by Fred at 12/23/2021 
Feature: Verify cart on Amazon
  # This is a testcase to verify cart on Amazon
  Scenario: User can verify cart
    Given Open Amazon homepage
    When User clicks on cart
    Then Verify empty cart