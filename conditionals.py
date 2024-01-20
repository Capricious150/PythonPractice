numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
names = ["Austin", "Derrick", "Adam", "Saph", "Bri", "Marcy", "Lee", "Tallons", "Paulina"]


# --- Aside ---
for name in names:
    if name == "Austin":
        print(name.title())
    
    elif name == "Lee":
        print(name.title())
    else: continue

# FINALLY I get to use elif. I've wanted elif for a while.
# Anyway, you know all this, it's 'if', 'elif', and 'else', and you use the colons for block scoping
# ------

# Equality checks (==) do not treat lower/upper as equals
print(names[0] == "austin")
# Gotta use them string methods
print(names[0].lower() == "austin")
# Inequality checks work as expected
print(names[0] != "austin")
# As do number comparisons
print(8 < 10)
print(8 <= 10)
print(8 == 10)
print(8 >= 10)
print(8 > 10)

# You can do inline multiple comparisons with 'and' and 'or'

print (names[0].lower() == 'austin' and 8 < 10)
print (8%2 == 0 or 8 < 6)

# You can check a List for the presence of a value with 'in' and 'not in'
if 'Aileen' not in names:
    print("You forgot your sister you hoser")

if 5 in numbers:
    print(numbers[4])

# Bools are capitalized
bool1 = True
bool2 = False

# Multiple elif chain

for number in range(1,16):
    if number%3 == 0 and number%5 == 0:
        print("FizzBuzz")
    elif number%3 == 0:
        print("Fizz")
    elif number%5 == 0:
        print("Buzz")
    else: continue

# Checking for emptyness in Lists is straightforward:

newList = []
if newList:
    print("List had content")
else: 
    print("Empty list")

# --- Aside ---
testNumber = 0
testString = ""

if testNumber:
    print("Number is True")
if testString:
    print("String is True")
# NEITHER condition above passed, meaning string and number emptyness works like in JS too
# ------
    
