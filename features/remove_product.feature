Feature: Remove Product
  In order to remove the products registered
  As a user
  I want to remove a product together with its category and company type

  Background: There is a registered user
    Given Exists a user "user" with password "password"
    And I login as user "user" with password "password"
    When I register product
      | name        |
      | Coca-Cola   |
    Then I'm viewing the details page for company by "user"
      | name        |
      | Coca-Cola   |
    And There are 1 Products

  Scenario: Remove just product name
    Given I login as user "user" with password "password"
    When I remove product
      | name        |
      | Coca-Cola   |
    Then I'm viewing the details page for company by "user"
      | name        |
      | Coca-Cola   |
    And There are 0 Products

  Scenario: Remove just product name and industry
    Given I login as user "user" with password "password"
    When I remove company
      | name        | industry     |
      | Coca-Cola   | Alimentation |
    Then I'm viewing the details page for company by "user"
      | name        | industry     |
      | Coca-Cola   | Alimentation |
    And There are 0 Companies

  Scenario: Try to remove company but not logged in
    Given I'm not logged in
    When I remove company
      | name        |
      | Coca-Cola   |
    Then I'm redirected to the login form
    And There are 1 Companies