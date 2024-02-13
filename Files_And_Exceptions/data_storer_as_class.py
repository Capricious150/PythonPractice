from pathlib import Path
import json

class Input_Storer:

    def __init__(self, pathstring) -> None:
        self.path = Path(pathstring)
    
    def check_read(self):
        print("Would you like to see the existing user inputs?")
        if input("Enter 1 for yes, and 2 for no: ") == "1":
            print(json.loads(self.path.read_text()))
        else: return None
    
    def new_content(self):
        user_input = input("Please enter new user input: ")
        contents = json.dumps(user_input)
        self.path.write_text(contents)
        self.check_read()

    def append_content(self):
        existing_content = self.path.read_text()
        destring = json.loads(existing_content)
        user_input = input("Please enter user input: ")
        contents = json.dumps(destring + "\n" + user_input)
        self.path.write_text(contents)
        self.check_read()

    def init_input(self):
        if self.path.exists():
            print("Existing content may already exist. Would you like to replace or append?")
            if input("Press 1 to append, and 2 to replace: ") == "1":
                self.append_content()
            else: self.new_content()
        else: self.new_content()
