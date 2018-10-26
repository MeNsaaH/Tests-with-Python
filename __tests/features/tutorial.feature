Feature: showing off behave
  
  @006_behave
  Scenario: run a simple test
    Given we have behave installed
    When we implement a test
    Then behave will test it for us!

  @006_behave
  Scenario: run a more complex test
    Given my_function exists
    Then it returns 'aaa' when run with 'a'

  @007_behave
  Scenario: Deleting a file
  Given the file "delete-me.txt" previously exists
  When the rm() function is called on the file "delete-me.txt"
  Then the file "delete-me.txt" ceases to exist