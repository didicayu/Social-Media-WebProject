Feature: Register Company
  In order to keep track of the companies registered
  As a user
  I want to register a company together with its industry type

  Background: There is a registered user
    Given Exists a user "user" with password "password"

  Scenario: Register just company name
    Given I login as user "user" with password "password"
    When I register company
      | name        |
      | Coca-Cola   |
    Then I'm viewing the details page for company by "user"
      | name        |
      | Coca-Cola   |
    And There are 1 Companies

  Scenario: Register just company name and industry
    Given I login as user "user" with password "password"
    When I register company
      | name        | industry     |
      | Coca-Cola   | Alimentation |
    Then I'm viewing the details page for company by "user"
      | name        | industry     |
      | Coca-Cola   | Alimentation |
    And There are 1 Companies

  Scenario: Try to register company but not logged in
    Given I'm not logged in
    When I register company
      | name        |
      | Coca-Cola   |
    Then I'm redirected to the login form
    And There are 0 Companies