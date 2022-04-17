Feature: User can open and switch windows in Amazon T&C page

  Scenario: User can open and close Amazon T&C page
   Given Open Amazon T&C page
   When Store original windows
   And Click on Amazon Privacy Notice link
   And Switch to the newly opened window
   Then Verify Amazon Privacy Notice page is opened
   And User can close new window and switch back to original
   #And switch back to original