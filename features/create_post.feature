
Feature: Create post
  In order to keep track of my posts
  As a user
  I want to create a post toghether with its product type
  Background: There are registered users
    Given Exists a user "user1" with password "password"


  Scenario: Register just post content
    Given I login as user "user" with password "password"
    When I post a post
      | content   |
      | Sketcher  |
    Then I'm viewing the details page for post by "user"
      | content   |
      | Sketcher  |
    And There are 1 post

  Scenario: Register just post content and product
    Given I login as user "user" with password "password"
    When I create a post
      | content      |  product |
      | Sketcher     |  shoe   |
    Then I'm viewing the details page for post by "user"
      | contnet      |  product |
      | Sketcher     |  shoe   |
    And There are 1 post

  Scenario: Try to register post but not logged in
    Given I'm not logged in
    When I post a post
      | content        |
      | The Tavern     |
    Then I'm redirected to create the login form
    And There are 0 posts