Feature: Create Post
  In order to keep track of the posts created
  As a user
  I want to create a post

  Background: There is a registered user
    Given Exists a user "user" with password "password"


  Scenario: Create post
    Given I login as user "user" with password "password"
    When I register company
      | name        | industry     |
      | Coca-Cola   | Alimentation |
    And I register product with company "Coca-Cola"
      | name        | category    | company     |
      | cola        | Drink       | Coca-Cola   |
    And I create post with product "cola"
      | content     | product    |
      | colaPost    | cola       |
    Then I'm viewing the details page for post "colaPost"
    Then There are 1 Posts


  Scenario: Try to create post but not logged in
    Given I'm not logged in
    When I register company
      | name        | industry     |
      | Coca-Cola   | Alimentation |
    And I register product
      | name        | category    | company     |
      | cola        | Drink       | Coca-Cola   |
    And I create post
      | content     | product    |
      | colaPost    | cola       |
    Then I'm redirected to the login form
    And There are 0 Posts