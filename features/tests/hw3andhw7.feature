# Created by Fred at 12/23/2021
Feature: Canceling Order on Amazon
  # This is a testcase to cancel order on Amazon
  Scenario: User can cancel order
    Given Open Amazon page
    When User types cancel order and submits
    Then Verify cancel order page