Feature: Remove Product
  In order to remove the products registered
  As a user
  I want to remove a product together with its category and company type

  Background: There is a registered user
    Given Exists a user "user" with password "password"
    And I login as user "user" with password "password"
    When I register product
      | name  |
      | shoe  |
    Then I'm viewing the details page for company by "user"
      | name   |
      | shoe   |
    And There are 1 Products

      Scenario: Register just product name
    Given I login as user "user" with password "password"
    When I register product
      | name        |
      | shoe        |
    Then I'm viewing the details page for product by "user"
      | name        |
      | shoe        |
    And There are 1 Products

  Scenario: Edit just product name and company
    Given I login as user "user" with password "password"
    When I edit product
      | name        | company     |
      | shoe        | Coca-Cola   |
    Then I'm viewing the details page for product by "user"
      | name        | company     |
      | shoe        | Coca-Cola   |
    And There are 1 Products

  Scenario: Edit just product name and company and category
    Given I login as user "user" with password "password"
    When I edit product
      | name        | company     | category |
      | shoe        | Coca-Cola   | drink    |
    Then I'm viewing the details page for product by "user"
      | name        | company     | category |
      | shoe        | Coca-Cola   | drink    |
    And There are 1 Products

  Scenario: Try to edit product but not logged in
    Given I'm not logged in
    When I edit product
      | name        |
      | Coca-Cola   |
    Then I'm redirected to the login form
    And There are 1 Products