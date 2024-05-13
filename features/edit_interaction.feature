Feature: Create user interaction
  In order to keep updated my previous registers about user interactions
  As a user
  I want to edit a user interaction I created
  Background: There are registered users and a post by one of them
    Given Exists a user "user1" with password "password"
    And Exists a user "user2" with password "password"
    And Exists post registered by "user1"
      | content   |
      | Sketcker  |
    And Exists interaction "comment" at post "sketcher" by "user2"
      | post      | interaction_type    | comment     |
      | Sketcher  | comment             | Buena foto  |

  Scenario: Edit a user interaction type "comment"
    Given I login as user "user2" with password "password"
    When I edit the user interaction for the post "Sketcher"
      | comment                         |
      | Que zapatillas mas chulas       |
    Then I'm viewing the details page for user interaction at post "sketcher" by "user2"
      | post      | interaction_type    | comment                   |
      | Sketcher  | comment             | Que zapatillas mas chulas  |
    And There are 1 posts

  Scenario: Try to edit user interaction but not logged in
    Given I'm not logged in
    When I view the details for user interaction for post "Sketcher"
    Then There is no "edit" link available

  Scenario: Try to edit post but not the owner
    Given I login as user "user1" with password "password"
    When I view the details for user interaction for post "Sketcher"
    Then There is no "edit" link available