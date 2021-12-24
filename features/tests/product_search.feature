# Created by Svetlana at 4/4/19
Feature: Test Scenarios for Search functionality

  Scenario: User can search for a product
    Given Open Google page
    When Input Watches into search field
    And Click on search icon
    Then Product results for Watches are shown

  Scenario: User can cancel order
    Given Open Amazon page
    When User types cancel order and submits
    Then Verify cancel order page