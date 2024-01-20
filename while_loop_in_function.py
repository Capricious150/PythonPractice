# This is not a lesson from the book, I just threw together some of what I've learned so far to make a (VERY) simple, user-input-driven, text-based calculator

def addition(int1 = 1, int2 = 1):
    return int1 + int2

def subtraction(int1 = 1, int2 = 1):
    return int1 - int2

def multiplication(int1 = 1, int2 = 1):
    return int1 * int2

def division (int1 = 1, int2 = 1):
    try:
        return int1 / int2
    except ZeroDivisionError:
        return "You divided by zero you clown"

def exponentiation (int1 = 1, int2 = 1):
    return int1 ** int2

def modulus(int1 = 1, int2 = 1):
    return int1 % int2

def check_for_ints(int1 = 1, int2 = 1):
    try:
        user_number1 = float(int1)
        user_number2 = float(int2)
        return True

    except ValueError:
        print("One or more invalid numbers were supplied. Please use numbers.")
        return False

def check_for_continue():
    response = input("Perform another operation? Enter 1 for yes, 2 for no:\n")
    while response != "1" and response != "2":
        response = input("Perform another operation? Enter 1 for yes, 2 for no:\n")
    if response == "1":
        return True
    else:
        return False

def calulator():
    valid_options = [1, 2, 3, 4, 5, 6, 7]
    choice = input("Hello. Please choose one of the following:\n1: Addition\n2: Subtraction\n3: Multiplication\n4: Division\n5: Exponentiation\n6: Modulus\n7: Quit \n")
    while True and float(choice) != 7:
        while check_for_ints(choice) == False or float(choice) not in valid_options:
            choice = input("Invalid entry. Please choose one of the following:\n1: Addition\n2: Subtraction\n3: Multiplication\n4: Division\n5: Exponentiation\n6: Modulus\n7: Quit \n")
        
        number_1 = input("Enter your first value: ")
        while check_for_ints(int1 = number_1) == False:
            number_1 = input("Enter your first value: ")
        number_2 = input("Enter your second value: ")
        while check_for_ints(int2 = number_2) == False:
            number_2 = input("Enter your second value: ")
        try:
            match float(choice):
                case 1:
                    print(addition(float(number_1), float(number_2)))
                    if check_for_continue() == True:
                        calulator()
                    else: return
                case 2:
                    print(subtraction(float(number_1), float(number_2)))
                    if check_for_continue() == True:
                        calulator()
                    else: return
                case 3:
                    print(multiplication(float(number_1), float(number_2)))
                    if check_for_continue() == True:
                        calulator()
                    else: return
                case 4:
                    print(division(float(number_1), float(number_2)))
                    if check_for_continue() == True:
                        calulator()
                    else: return
                case 5:
                    print(exponentiation(float(number_1), float(number_2)))
                    if check_for_continue() == True:
                        calulator()
                    else: return
                case 6:
                    print(modulus(float(number_1), float(number_2)))
                    if check_for_continue() == True:
                        calulator()
                    else: return
                case 7:
                    return
                case _:
                    return
        except Exception as e:
            print(f"Something broke. Python thinks it's {e}")
        else:
            print(f"Honestly, I have no idea what happened. You shouldn't see this text.")

response = calulator()
if response != None:
    print(response)