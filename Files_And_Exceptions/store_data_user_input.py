from pathlib import Path
import json

path = Path('user_input.json')

# contents = input("Write literally anything and then hit enter. For demonstration purposes, it will be better if you enter something other than just whitespace: ")
# response_string = json.dumps(contents)
# path.write_text(response_string)
# print(path.read_text())

def new_content():
    user_input = input("Please enter new user input: ")
    contents = json.dumps(user_input)
    path.write_text(contents)
    check_read()

def append_content():
    existing_content = path.read_text()
    destring = json.loads(existing_content)
    user_input = input("Please enter user input: ")
    contents = json.dumps(destring + "\n" + user_input)
    path.write_text(contents)
    check_read()


def check_read():
    print("Would you like to see the existing user inputs?")
    if input("Enter 1 for yes, and 2 for no: ") == "1":
        print(json.loads(path.read_text()))
    else: return None

if path.exists():
    print("Existing content may already exist. Would you like to replace or append?")
    if input("Press 1 to append, and 2 to replace: ") == "1":
        append_content()
    else: new_content()
else: new_content()