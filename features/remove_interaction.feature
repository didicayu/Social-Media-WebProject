Feature: Remove Interaction
  In order to keep track of the interactions registered
  As a user
  I want to edit an interaction

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
    And I create like interaction for post "colaPost"
      | post        |interaction_type |
      | colaPost    | like            |
    Then There are 1 Interactions

  Scenario: Remove Interaction
    Given I login as user "user" with password "password"
    When I remove interaction in post "colaPost"
    Then There are 0 Interactions

  Scenario: Try to remove interaction but not logged in
    Given I'm not logged in
    When I remove interaction in post "colaPost"
    Then I'm redirected to the login form

