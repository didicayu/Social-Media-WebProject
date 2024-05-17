Feature: Edit Post
  In order to keep track of the posts registered
  As a user
  I want to edit a post

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
      | cola_Post   | cola       |
    Then There are 1 Posts

  Scenario: Edit company
    Given I login as user "user" with password "password"
    When I edit the post with the name "cola_Post"
      | content     | product    |
      | fanta_post  | fanta      |
    Then I'm viewing the details page for post "fanta_post"
      | content     | product    |
      | fanta_post  | fanta      |
    And There are 1 Posts

  Scenario: Try to edit post but not logged in
    Given I'm not logged in
    When I'm viewing the details page for company by "user"
    Then I'm redirected to the login form

