Feature: Remove Company
  In order to remove the companies registered
  As a user
  I want to remove a company together with its industry type

  Background: There is a registered user
    Given Exists a user "user" with password "password"
    And I login as user "user" with password "password"
    When I register company
      | name        | industry     |
      | Coca-Cola   | Alimentation |
    Then There are 1 Companies


  Scenario: Remove company
    Given I login as user "user" with password "password"
    When I remove company
      | name        | industry     |
      | Coca-Cola   | Alimentation |
    Then There are 0 Companies


   Scenario: Try to remove company but not logged in
    Given I'm not logged in
    When I remove company
      | name        | industry     |
      | Coca-Cola   | Alimentation |
    Then There are 1 Companies
    And I'm redirected to the login form
