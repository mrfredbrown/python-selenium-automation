# Created by Fred at 4/17/2022
Feature: Logged out user sees Sign in page
  # Enter feature description here

  Scenario: Logged out user sees Sign in page when clicking Orders
    Given Open Amazon page
    When Click Amazon Orders link
    Then Verify Sign In page is opened
