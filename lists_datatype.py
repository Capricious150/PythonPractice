# Indexed data collections are called Lists in Python
# Naming convention is to end them with an "s". They are initialized with square brackets

coins = ["penny","nickel","dime","quarter"]

# Individual items are accessed just like in JS. Lists are 0-indexed
print(coins[0])
print(coins[3])

m = f"I just lost a {coins[3]} of my life savings thanks to a collapsed {coins[1]} mine"
print(m)

# List elements can be changed by direct assignment
coins[2] = "mini-nickel"

# Lists can have a new value added at the end with .append()
coins.append("dime")

# Lists can have a new value added at a specific index with .insert(), pushing the replaced element and all following elements 1 index position to the right
coins.insert(1, "demi-nickel")
print(coins)

# A specific indexed element can be deleted with the 'del' statement. This is not an List method, and has no return. 
# The remaining elements following the deleted element will shift 1 index position to the left
del coins[3]
print(coins)

# List.pop() without an argument works just like in JS
q = coins.pop()
print(q)
print(coins)

# List.pop(num) can take an int argument, and pop the targeted index position
dn = coins.pop(1)
print(dn)
print(coins)

# List.remove(arg) removes a given value from a List, agnostic to its index position. It will only remove the first matching value found.
coins.remove('nickel')
print(coins)

# The .sort() method permanently sorts a List
letters = ['g', 'y', 'a', 'd', 'h', 'o', 'v', 'k']
letters.sort()
print(letters)
# The .sort method accepts the argument 'reverse=True' to reverse-sort
numbers = [0, 2, 1, 4, 7, 6, 8, 9, 3]
numbers.sort(reverse=True)
print(numbers)

# The "sorted(List)" function returns a new List which is just the provided List, sorted
print(sorted(numbers))

# List.reverse() reverses the order of the List.
numbers.reverse()
print(numbers)

# The len(List) function returns the length of a List.
print(len(numbers))

# min(list), max(list), and sum(list) do what you'd expect, finding the smallest and largest values in an array, as well as their sum
print(min(numbers))
print(max(numbers))
print(sum(numbers))

# you can skip both ints to just iterate over the whole array. This is useful when creating deep copies of lists
numbersCopy = numbers[:]
# (As opposed to a shallow copy, which would be something like numbersCopy = numbers)