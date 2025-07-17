# Created by joker at 7/16/2025
Feature: Off-Plan
  # Enter feature description here

  Scenario: Testing of-plan has proper options available
    Given open reelly https://soft.reelly.io/sign-in
    When click on off-plan menu button
    And click first off-plan listing
    Then verify visualization options
