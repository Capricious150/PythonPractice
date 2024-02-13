from basic_function import read_back

while True: 
    fname = input("Enter your first name: ")
    lname = input("Enter your last name: ")
    response = read_back(fname, lname)
    print(response)
    break