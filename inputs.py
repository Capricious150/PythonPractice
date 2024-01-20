spacer = "============"

# print(spacer)
# print("Hello.")
# username = input("Please enter your username: ")
username = "Austin"
# print(f"Thank you, {username}.\nHave a nice day")
# print(spacer)

# the int() function can toInt a string in
a = "21"
b = int(a)
# print(b)
# (WORKS)

c = "Cornish"
# d = int(c)
# print(d)
# (BREAKING ERROR)


print(spacer)
print("Hello. This application will add or subtract two values.")

option = input("Would you like to Add or Subtract? ")
while option.lower() != "add" and option.lower() != "subtract":
    option = input("Invalid input. Please enter 'Add' or 'Subtract' (not case sensitive)")

while True:
    val1 = input("Enter value 1: ")
    
    try:
        val1_int = int(val1)
        break
    
    except ValueError:
        print("Please enter an integer")

while True:
    val2 = input("Enter value 2: ")

    try:
        val2_int = int(val2)
        break

    except ValueError:
        print("Please enter an integer")

if (option.lower() == "add"):
    print(f"{val1_int} plus {val2_int} equals {val1_int + val2_int}")
elif (option.lower() == "subtract"):
    print(f"{val1_int} minus {val2_int} equals {val1_int - val2_int}")
else: 
    print("Something went wrong")

print(spacer)