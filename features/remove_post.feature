Feature: Remove Post
  In order to keep track of the Posts registered
  As a user
  I want to remove a post

  Background: There is a registered user
    Given Exists a user "user" with password "password"
    And I login as user "user" with password "password"
    When I register company
      | name        | industry     |
      | Coca-Cola   | Alimentation |
    And I register product with company "Coca-Cola"
      | name        | category    | company     |
      | cola        | Drink       | Coca-Cola   |
    And I create post with product "cola"
      | content     | product    |
      | colaPost    | cola       |
    Then There are 1 Posts

  Scenario: Remove Post
    Given I login as user "user" with password "password"
    When I remove post
      | content     |
      | colaPost    |
    Then There are 0 Posts

  Scenario: Try to remove post but not logged in
    Given I'm not logged in
    When I remove post
      | content     |
      | colaPost    |
    Then I'm redirected to the login form
    And There are 1 Posts

