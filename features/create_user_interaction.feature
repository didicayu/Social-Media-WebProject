Feature: Create user interaction
  In order to keep track of my user interactions
  As a user
  I want to create a user interaction
  Background: There are registered users and a post by one of them
    Given Exists a user "user1" with password "password"
    And Exists a user "user2" with password "password"
    And Exists post registered by "user1"
      | content   |
      | Sketcker  |

  Scenario: Create a user interaction
    Given I login as user "user2" with password "password"
    When I create a user interaction "comment" at post "Sketcher"
      | interaction_type    | comment     |
      | comment             | Buena foto  |
    Then I'm viewing the details page for user interaction at post "sketcher" by "user2"
      | post    | interaction_type    | comment     |
      | Sketcker| comment             | Buena foto  |
    And There are 1 post

  Scenario: Try to create user interaction but not logged in
    Given I'm not logged in
    When I create the user interaction for post "Sketcher"
    | interaction_type    | comment     |
    | comment             | Buena foto  |
    Then I'm redirected to the login form
    And There are 0 posts