Feature: Create Interaction
  In order to keep track of the interactions created
  As a user
  I want to create an interaction

  Background: There is a registered user
    Given Exists a user "user" with password "password"


  Scenario: Create Interaction
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
    And I create like interaction for post "colaPost"
      | post        |interaction_type |
      | colaPost    | like            |
    Then I'm viewing the details page for interaction in post "colaPost"
      | post        |interaction_type |
      | colaPost    | like            |
    And There are 1 Interactions
    And There are 1 likes in post "colaPost"


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