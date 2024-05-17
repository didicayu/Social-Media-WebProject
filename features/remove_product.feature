Feature: Remove Product
  In order to keep track of the companies registered
  As a user
  I want to edit a company

  Background: There is a registered user
    Given Exists a user "user" with password "password"
    And I login as user "user" with password "password"
    When I register company
      | name        | industry     |
      | Coca-Cola   | Alimentation |
    And I register product with company "Coca-Cola"
      | name        | category    | company     |
      | cola        | Drink       | Coca-Cola   |
    Then There are 1 Products

  Scenario: Remove Product
    Given I login as user "user" with password "password"

    When I remove product
      | name        |
      | cola        |
    Then There are 0 Products

  Scenario: Try to remove product but not logged in
    Given I'm not logged in
    When I remove product
      | name        | category    | company     |
      | cola        | Drink       | Coca-Cola   |
    Then I'm redirected to the login form

