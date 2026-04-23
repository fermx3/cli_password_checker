# Password Checker

## Description
This tool receives a password safely and checks its strength rated from 0 to 10.
The password is entered securely and never displayed on screen.
Also you will receive feedback on how to improve your password.

## Requirements
Python 3.10+ (no external dependencies)

## Installation

  `git clone https://github.com/fermx3/cli_password_checker.git && cd cli_password_checker`

## Usage
To use it you have to call main.py and pass the password when prompted

Example:
`python main.py`

## Output Example
```
Password received.

---------- Results: ----------
Score: 5/10 █████░░░░░ Normal
------------------------------

- Add at least one uppercase letter (A-Z)
- Add at least one digit (0-9)
- Add at least one special character (!@#$%^&*)
```
