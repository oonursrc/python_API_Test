Feature: SignUp

    Scenario Outline: Verify Delete API functionality
        Given Delete User API is going to be executed
        When Query User and Delete User API executed with for an existing user <username>
        Then Delete User for <username> is successful
        Examples:
        |username|
        |Ali |