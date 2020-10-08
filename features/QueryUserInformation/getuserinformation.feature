Feature: Query User Information

    Scenario Outline: Verify user information query API functionality
        Given Query User Information is going to be executed
        When Query User Information API executed with <username>
        Then Query operation for <username> is successful
        Examples:
        |username|
        |admin|
        |dev  |


    Scenario Outline: Verify user information query API functionality if user not exist
        Given Query User Information is going to be executed
        When Query User Information API executed for nonexising user <username>
        Then Query operation for <username> returns 404
        Examples:
        |username|
        |elma|


    Scenario Outline: Verify user information query API functionality with wrong query parameter
        Given Query User Information is going to be executed
        When Query User Information API executed for <username> with wrong query parameter
        Then Query operation for <username> returns 400
        Examples:
        |username|
        |elma|