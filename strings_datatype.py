message_1 = "Hello World"
print(message_1)

message_1 = "Hello Kevin"
print (message_1)

# Variable names may contain letters, numbers, and underscores, but may not start with a number

# Strings:
# Strings can use "double" or 'single' quotes
# Rules seem to be just like JavaScript

# String Methods:
# STRING.title() -- Proper Noun casing
name = "austin andrews"
print(name.title())

#STRING.upper() and STRING.lower() do what you'd expect
print(name.upper())
print(name.lower())

#In Python, 'format strings' are what in JS are 'string template literals'.
fname = "austin"
lname = "andrews"
name = f"{fname} {lname}"
print(name.title())
message = f"Hello, {name.title()}, how are you today?"
print(message)

# \t and \n can be used for tab-space and new line, respectively
# \t uses those fancy tabs where instead of adding a fixed number of spaces, it adds whitespace until it gets to a new length of 8 characters
message_1 = "Salt:\t2\nPepper:\t6\nOregano:\t0"
print(message_1)

# rstrip() method removes trailing whitespace from the end of a string
# There also exists lstrip() and strip(), with the latter doing both ends of a string
message_1 = "Example one     "
message_2 = "     Emample two"
message_3 = "     Example three     "
print(message_1.rstrip() + message_2.rstrip() + message_3.rstrip())

# removeprefix(str) accepts a string argument, and removes it from the from of a string
message_1 = "http://www.archaicurlformat.com/"
print(message_1.removeprefix('http://www.'))
print(message_1.removesuffix('.com'))
print(message_1.removeprefix('http://www.').removesuffix('.com/'))
print(message_1.removeprefix('foobar'))