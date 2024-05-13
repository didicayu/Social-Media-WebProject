Feature: Delete user interaction
  In order to keep updated my previous registers about user interactions
  As a user
  I want to delete a user interaction I created
  Background: There are registered users and a post by one of them
    Given Exists a user "user1" with password "password"
    And Exists a user "user2" with password "password"
    And Exists post registered by "user1"
      | content   | likes   | shares  |   comments  |
      | Sketcker  | 120     | 12      |   2         |
    And Exists interaction "like" at post "Sketcher" by "user2"
      | post      | interaction_type    |
      | Sketcher  | like                |

  Scenario: Delete user interaction type "like"
    Given I login as user "user2" with password "password"
    When I delete the user interaction "like" for the post "Sketcher" by "user2"
    Then I edit the post "Sketcher" by "user1"
    | content   | likes   | shares  |   comments  |
    | Sketcker  | 119     | 12      |   2         |
    And There are 0 user interactions "like" for post "Sketcher" by "user2"

  Scenario: Delete user interaction type "share"
    Given I login as user "user2" with password "password"
    When I delete the user interaction "share" for the post "Sketcher" by "user2"
    Then I edit the post "Sketcher" by "user1"
      | content   | likes   | shares  |   comments  |
      | Sketcker  | 119     | 11      |   2         |
    And There are 0 user interactions "share" for post "Sketcher" by "user2"

  Scenario: Delete user interaction type "comment"
      Given I login as user "user2" with password "password"
      When I delete the user interaction "comment" for the post "Sketcher" by "user2"
      Then I edit the post "Sketcher" by "user1"
      | content   | likes   | shares  |   comments  |
      | Sketcker  | 119     | 11      |   1         |
    And There are 0 user interactions "comment" for post "Sketcher" by "user2"


  Scenario: Try to edit user interaction but not logged in
    Given I'm not logged in
    When I view the details for user interaction for post "Sketcher"
    Then There is no "edit" link available

  Scenario: Try to edit post but not the owner
    Given I login as user "user1" with password "password"
    When I view the details for user interaction for post "Sketcher"
    Then There is no "edit" link available