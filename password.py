from getpass import getpass

username = input("Enter username: ")
password = getpass("Enter password: ")

print("Logging in.....")

#*********************************************

import os

user_id=os.environ.get("USER_ID")
user_pass=os.environ.get("USER_PASS")

print(user_id)
print(user_pass)