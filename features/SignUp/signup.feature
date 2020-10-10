Feature: SignUp

    Scenario Outline: Verify signup API functionality
        Given SignUp is going to be executed
        When SignUp API executed with for a new user with <info_dict> infos
        Then Signup and query operation for <username> is successful
        Examples:
        |info_dict|username|
        |{"username": "Onur","isAdmin": true,"dateOfBirth": "1989-11-08","email": "a@b.com","name": "Onur S","password": "a123","superpower": "ciko"}|Onur|
        |{"username": "Ali","isAdmin": false,"dateOfBirth": "1995-03-12","email": "c@d.com","name": "Ali M","password": "m111","superpower": "fiko"} |Ali |
        |{"username": "Veli","isAdmin": false,"dateOfBirth": "19801105","email": "a@f.com","name": "Veli A","password": "qw12","superpower": "swim"} |Veli|
        |{"username": "Ayse","isAdmin": false,"dateOfBirth": "1999-07-09","email": "what","name": "Ayse E","password": "bv55633fddf3","superpower": "runn"} |Ayse|
        |{"username": "Melis","isAdmin": false,"dateOfBirth": "1999-07-09","email": "*+/","name": "Melis","password": "112233","superpower": "jumpp"} |Melis|