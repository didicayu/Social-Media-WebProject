Feature: Edit Company
  In order to keep track of the companies registered
  As a user
  I want to edit a company

  Background: There is a registered user
    Given Exists a user "user" with password "password"
    And I login as user "user" with password "password"
    When I register company
      | name        | industry     |
      | Coca-Cola   | Alimentation |
    Then There are 1 Companies

  Scenario: Edit company
    Given I login as user "user" with password "password"
    When I edit the company with the name "Coca-Cola"
      | industry     |
      | Alimentation |
    Then I'm viewing the details page for company by "user"
      | name        | industry     |
      | Coca-Cola   | Alimentation |
    And There are 1 Companies

  Scenario: Try to edit company but not logged in
    Given I'm not logged in
    When I register company
      | name        | industry     |
      | Coca-Cola   | Alimentation |
    Then I'm redirected to the login form
    And There are 0 Companies

  Scenario: Try to edit company but not logged in
    Given I'm not logged in
    When I view the details for company "Coca-Cola"
    Then I'm redirected to the login form

