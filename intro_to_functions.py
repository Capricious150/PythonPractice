# (This is for a different lesson file, but this is an import from a default library)
from datetime import datetime


# Functions are declared with "def"
# Parameters can be given default values in the function definition
# Parameters without default values must go before parameters with default values
# Function calls can optionally specify which argument is being given, or can use positional arguments


str_name = "Austin"

def basic_function(adjective='gigantic', name='Jane', adjective2=''):
    # Prints "Hello"
    message = f"Hello, {name.title()}, you're looking very {adjective.lower()} today"
    vowels = ['a', 'e', 'i', 'o', 'u']

    if adjective2 and adjective2[0].lower() in vowels:
        message += f"\nI hope you have an {adjective2.lower()} day."
    elif adjective2:
        message+= f"\nI hope you have a {adjective2.lower()} day"
    return message

# print(basic_function(adjective="handsome", name=str_name))
# print(basic_function("John", "generic"))
# print(basic_function('vivid'))
# print(basic_function())
# print(basic_function(name=str_name))
# print(basic_function(name="Austin", adjective="Handsome", adjective2="Great"))
# print(basic_function("smart", "austin", "astounding"))

def a_dict(name='USER', color='RED'):
    
    dt = datetime.now()
    profile = {
        'NAME': name.upper(),
        'FAVORITE_COLOR': color.upper(),
        'CREATED': f"{dt.month}-{dt.day}-{dt.year} {dt.hour}:{dt.minute}"
    }

    return profile

# print(a_dict('sam', 'blue'))

numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

# You can pass a list to a function
def read_list(li):
    for value in li:
        print(value)

read_list(numbers_list)
# You can also send a shallow copy of a List to prevent the original list from being Modified:
def shift_list(li):
    new_numbers = []
    for index in range(len(li)):
        new_numbers.append(2 * li.pop())
    print(new_numbers)

shift_list(numbers_list[:])
# If I sent (numbers_list) rather than (numbers_list[:], the above function would empty the original list out)
print(numbers_list)


# You can pass an arbitrary number of arguments to a function like so:
def add_toppings(*toppings):
    message = "I want a pizza with "
    for topping in toppings:
        message += f"{topping}, "
    message += "and cheese."
    return message

# Note that rather than sending an list of strings, I'm sending 4 strings
print(add_toppings('pineapple', 'bell pepper', 'sausage', 'olives'))
# If I send a list, it doesn't work as expected, because on the recieving end it gets a List with a length of 1, where at index position 0 appears the entire supplied list
print(add_toppings(['pineapple', 'bell pepper', 'sausage', 'olives']))

# Arbitrary Arguments must come LAST in the parameters list

def mix_n_match (name, age = 21, *favorites ):
    message = f"I am {name}, I'm {age} years old, and my favorite things are: "
    for thing in favorites:
        message += f"{thing}, "
    return message

print(mix_n_match('Austin', 34, "Eggs", "Caffeine", "Sleep"))
# Note that, while I've provided a default position for age, it won't matter unless I specify my arguments
print(mix_n_match('Austin', "Eggs", "Caffeine", "Sleep"))

# aribtrary keyword arguments, or **kwargs, are entered as KVPs

def built_a_person(name, age, **kwargs):
    person = {
        "name": name,
        "age": age,
    }

    for key, value in kwargs.items():
        person[f"{key}"] = value

    return person

print(built_a_person('Austin', 34, favorites="Sleep", shirt_color="Red"))
# Note that the below would NOT work, as it has repeating keywords. I'd need to build the function to handle kwarg lists, and THEN send favorites = ['Sleep', 'Food']
# print(built_a_person('Austin', 34, favorites="Sleep", favorites="Food", shirt_color="Red"))