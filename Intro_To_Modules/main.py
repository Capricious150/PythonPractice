# Entire modules can be imported, and their contents can be accessed via dot-notation
import say_hello
print(say_hello.say_hello("Sam"))

# Expecific elements of modules can be imported
from say_hi import say_hi
print(say_hi("Austin"))

# Imported elements can be given aliases
from say_bonjour import say_bonjour as bonjour
print(bonjour("Aileen"))

# Modules can also be given aliases
import say_hola as hola
print(hola.say_hola("Adam"))

# All elements of a module can also be imported at once
from say_more import *
print(say_salud("Derrick"))
print(say_fuck_off("Steve"))
print(say_ahoy("me hearties"))

