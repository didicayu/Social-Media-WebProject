Feature: Edit Product
  In order to keep track of the products registered
  As a user
  I want to edit a product

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

  Scenario: Edit Product
    Given I login as user "user" with password "password"

    When I edit the product with the name "cola"
      | category     |
      | Energy drinkn|
    Then I'm viewing the details page for product "cola"
      | name        | category    | company     |
      | cola        | Energy drink| Coca-Cola   |
    And There are 1 Companies

  Scenario: Try to edit product but not logged in
    Given I'm not logged in
    When I edit the product with the name "cola"
    Then I'm redirected to the login form

