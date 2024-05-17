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
      | colaPost    | cola       |
    Then There are 1 Posts

  Scenario: Edit post
    Given I login as user "user" with password "password"
    When I edit the post "colaPost"
      | content     | product    |
      | colaPostEDIT| cola       |
    Then I'm viewing the details page for post "colaPostEDIT"
      | content     | product    |
      | colaPostEDIT| cola       |
    And There are 1 Posts

  Scenario: Try to edit post but not logged in
    Given I'm not logged in
    When I edit the post "colaPost"
      | content     | product    |
      | colaPostEDIT| cola       |
    Then I'm redirected to the login form

