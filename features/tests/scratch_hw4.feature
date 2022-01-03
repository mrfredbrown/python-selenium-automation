# Created by Fred at 12/23/2021
Feature: User can open Amazon best seller's webpage
  # This is a testcase to cancel order on Amazon
  Scenario: User can open Amazon best seller's webpage
    Given Open Amazon best seller webpage
    When User clicks on bestseller
    Then Verify bestseller page

