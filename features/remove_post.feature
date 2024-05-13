Feature: Remove Post
  In order to remove one of my posts
  As a user
  I want to remove a post toghether with its product type
  Background: There are registered users
    Given Exists a user "user" with password "password"
    And I login as user "user" with password "password"
    When I post a post
      | content   |
      | sketcker  |
    Then I'm viewing the details page for post by "user"
      | content   |
      | Sketcker  |
    And There are 1 posts


  Scenario: Remove just post content
    Given I login as user "user" with password "password"
    When I remove a post
      | content   |
      | sketcker  |
    Then I'm viewing the details page for post by "user"
      | content   |
      | Sketcker  |
    And There are 0 posts

  Scenario: Remove just post content and product
    Given I login as user "user" with password "password"
    When I remove a post
      | content      |  product |
      | Sketcher     |  shoes   |
    Then I'm viewing the details page for post by "user"
      | contnet      |  product |
      | Sketcher     |  shoe   |
    And There are 0 posts

  Scenario: Try to remove post but not logged in
    Given I'm not logged in
    When I remove a post
      | content        |
      | The Tavern     |
    Then I'm redirected to the login form
    And There are 1 posts