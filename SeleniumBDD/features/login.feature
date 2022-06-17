Feature: Ultimateqa login
  Scenario: Login to Ultimateqa with valid parameters
    Given launch browser
    When open home page
    And navigate to atutomation execises
    And click on "Login automation"
    And  validate the title of the page
    And Enter username "ss@gmail.cpm" and password "qwertyuiop657"
    Then User must be successfully login to the website