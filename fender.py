# python-fender-challenge (For Reference)

# Important. When parsing, default is write. Make sure to set to either set to w/r/a.
# Remember to use .DictReader/Writer when parsing hash (dictionary).

import csv
import json

compromised_users = []

with open('passwords.csv', newline='') as password_file:
  password_csv = csv.DictReader(password_file)
  for password_row in password_csv:
    # password_row['Username'] being the key of the dict password_csv
    compromised_users.append(password_row['Username'])

with open('compromised_users.txt', 'w') as compromised_user_file:
  for user in compromised_users:
    compromised_user_file.write(user)

# Code below to check for .txt file content:

# with open('compromised_users.txt') as text_file:
#   text_data = text_file.read()
# print(text_data)


with open('boss_message.json', 'w') as boss_message:
  boss_message_dict = {
    "recipient" : "The Boss",
    "message" : "Mission Success"
  }
  json.dump(boss_message_dict , boss_message)

# Code below to check for .json file content:

# with open('boss_message.json') as boss_message:
#   message = json.load(boss_message)
	 
# print(message['recipient'])
# print(message['message'])


	with open('new_passwords.csv', 'w') as new_passwords_obj:
    slash_null_sig = "Slash Null"
	  new_passwords_obj.write(slash_null_sig)
