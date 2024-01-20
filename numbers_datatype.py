# Integers are integers. They can be exponentiated, divided, multiplied, added, and subtracted

z, y = 1, 3
x = z + (y * y)
print(x * (y - z))
print((y ** (y + z))/y) 

# Any number with a decimal is a Float
# Any use of division, even one which results in a whole number, produces a Float and not an Int
# Any operation which uses a mix of Ints and Floats will result in a Float
# SYNTACTICAL SUGAR: Underscores are ignored in Numbers, allowing for: 1_000_000_000_000_000 (1 Quadrillion) instead of 1000000000000000

# Multiple assignments are cool, can I do this in JS?
x, y, z = 1, 2, 3
a, b, c = "I bought", (x+y+z), "pickles"
message = f"{a} {b} {c}."
print(message)

# Variables which should be treated as constant use ALL_CAPS
# This doesn't actually make them constant, it just kind of tells other programmers your intent

CONTANT_VALUE = 5000
print(CONTANT_VALUE)
CONTANT_VALUE = 6000
print(CONTANT_VALUE)
