Feature: Ultimateqa title check
  Scenario: Checking title of ultimateqa.com
    Given launch browser
    When open ultimateqa.com homepage
    Then verify that title is "Home | Ultimate QA"
    And close browser
