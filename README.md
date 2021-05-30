# login_system
A system for logins and signups 
- can sign up following standard sign up conditions (passwoard chars, username length, email format, etc.)
- it stores your email, username and password, allows you to sign back in after closing/reopening

to reuse properly, a user_logs.txt file must be created in the same directory - works best if a first suer is already initialized with the following code:

import json

user_logs = [{"email": "email@email.com", "username": "user_name", "password": "Aa12345*"}]

with open("user_logs.txt", "w") as log:
    json.dump(user_logs, log)



Package    Version
---------- -------
pip        21.0.1
setuptools 56.0.0


Python 3.8.5 
