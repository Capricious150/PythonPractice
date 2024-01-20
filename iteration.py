numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
names = ["Austin", "Derrick", "Adam", "Saph", "Bri", "Marcy", "Lee", "Tallons", "Paulina"]

# Similar to a for...in loop in JS
for number in numbers:
    # Indentation matters in Python!! It functions like {} in other languages to determine block scoping
    product = number * 3
    message = f"{number} times 3 is {product}"
    print(message)

print("The loop has concluded")

# A FOR LOOP can use range(num, num) to iterate over a set group of numbers
# Note that the second argument acts as an upper bound, and is not included in the iteration
for value in range(1, 5):
    print(value) 
    # prints 1 2 3 4

#Note that range() can also be supplied just 1 number, and will iterate 0 - NUM
for value in range(5):
    print(value)
    # prints 0 1 2 3 4

# A range() can be converted directly to a List with the list(arg) function
values = list(range(10))
print(values)

# range() can be given a 3rd argument to act as a step count
values = list(range(1, 11, 2))
# [1, 3, 5, 7, 9]
print(values)
values = list(range(1, 11, 3))
# [1, 4, 7, 10]
print(values)

# --- Aside ---
# This isn't a lesson, I was just messing around with len()
outputs = []
for value in range(11):
    outputs.append(value)
    outputLength = len(outputs)
    outputs[0] += outputLength
print(outputs)
# ------


# min(list), max(list), and sum(list) do what you'd expect, finding the smallest and largest values in an array, as well as their sum
print(min(numbers))
print(max(numbers))
print(sum(numbers))

# A new (to me) Python concept is the List Comprehension, which combines a FOR loop with an implicit return to assign value immediately
# In the following example, I will use List Comprehension to create a List of squares in one line:

squares = [number**2 for number in numbers]
# <== RETURN FROM for variable in variables
print(squares)

# "To use this syntax, declare a variable. Next open a set of square brackets and define the expression for the values you want to store
#  in the new List. In the above example, the expression is 'number**2', which is being fed numbers from a for loop to its right"
#  Python Crash Course, 3rd Ed, pg 60 (Heavily paraphrased)

# A range of values can be shorthanded with [ind1:ind2]. For example:
print(numbers[2:6])
# In the above example, print() will operate on the numbers List, index positions 2 through 5, with 6 acting as a non-included upper bound
# If you are starting at index position 0, you don't need to supply the first int
print(squares[:3])
# Similarly, by skipping the second int, you will go until the end of the List
print(numbers[3:])
# You can also use negative ints for omissions
# For example, starting with a -2 will start the iteration from the 2nd-to-last index
print(numbers[-2:]) 
# While ending with a -2 will treat the 2nd-to-last intex as an upper bound
print(numbers[:-2])

# These shorthands can be used in FOR loops
for number in numbers[1:-2]:
    print(number)

# Lastly, you can skip both ints to just iterate over the whole array. This is useful when creating deep copies of lists
numbersCopy = numbers[:]
# (As opposed to a shallow copy, which would be something like numbersCopy = numbers)

# Tuples are Immutable Lists. They are declared using parens instead of square brackets
dimensions = (800, 640)
# They can be read like Lists, but cannot be written to after they have been initialized
# Tuples are immutable, but not constants. They can be written over:
dimensions = (700, 500)

# --- Aside ---
# Note: The parens are not actually the thing that makes a tuple, it's the comma and lack of square brackets
isThisATuple = 14, 5, 6, 2
print(isThisATuple[2])

# Thus, to declare a single value tuple you could do:
tuple3 = 2,
tuple4 = (5,)

print(tuple3[0])
print(tuple4[0])
# While this technically works, use the parens. They're needed for readability.
# ------

