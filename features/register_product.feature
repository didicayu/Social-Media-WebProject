Feature: Register Product
  In order to keep track of the products registered
  As a user
  I want to register a product together with its category and company type

  Background: There is a registered user
    Given Exists a user "user" with password "password"


  Scenario: Register product
    Given I login as user "user" with password "password"
    When I register company
      | name        | industry     |
      | Coca-Cola   | Alimentation |
    And I register product with company "Coca-Cola"
      | name        | category    | company     |
      | cola        | Drink       | Coca-Cola   |
    Then I'm viewing the details page for product "cola"
    And There are 1 Products


  Scenario: Try to register product but not logged in
    Given I'm not logged in
    When I register product
      | name        | category    | company     |
      | cola        | Drink       | Coca-Cola   |
    Then I'm redirected to the login form
    And There are 0 Products