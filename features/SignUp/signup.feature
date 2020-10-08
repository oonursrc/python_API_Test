Feature: SignUp

    Scenario Outline: Verify signup API functionality
        Given SignUp is going to be executed
        When SignUp API executed with for a new user with <info_dict> infos
        Then Signup and query operation for <username> is successful
        Examples:
        |info_dict|username|
        |{"username": "Onur","isAdmin": true,"dateOfBirth": "1989-11-08","email": "a@b.com","name": "Onur S","password": "a123","superpower": "ciko"}|Onur|
        |{"username": "Ali","isAdmin": false,"dateOfBirth": "1995-03-12","email": "c@d.com","name": "Ali M","password": "m111","superpower": "fiko"} |Ali |