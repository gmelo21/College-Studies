# You know what? I have never done a calculator in Python before. And I feel like it's kind of tradition to do so. So...
# Going to come back to this soon. Only then, with GUI. Be prepared. (It's going to be the simplest thing ever.)
# Also, this is just a study about try, except, else and finally. The calculator is for flavor.

import time

def ask_for_numbers():
        global a
        global b
        while True:
            try:
                a = int(input("First number: "))
                break
            except ValueError:
                print("Could I be any clearer? A NUMBER.")
        while True:
            try:
                b = int(input("Second number: "))
                break
            except ValueError:
                print("Could I be any clearer? A NUMBER.")

def sum(a, b):
    return a + b

def subtract(a, b):
    return a - b

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Don't try to break my calculator! No dividing by zero!")

def multiply(a, b):
    return a * b

while True:
    try:
        print()
        print("1 - Sum")
        print("2 - Subtract")
        print("3 - Divide")
        print("4 - Multiply")
        print("0 - End")
        operation = int(input("\nChoose your operation: "))
    except ValueError:
        print("That's not even a number!")
    else:
        match operation:
            case 1:
                ask_for_numbers()
                print(sum(a, b))
            case 2:
                ask_for_numbers()
                print(subtract(a, b))
            case 3:
                ask_for_numbers()
                print(divide(a, b))
            case 4:
                ask_for_numbers()
                print(multiply(a, b))
            case 0:
                break
            case _:
                print("Type one of the numbers displayed, please...")
        time.sleep(1.5)

try:
    choice = int(input("\nType a number to get a nice message, or anything else for a mean message."))
    print("You look nice today.")
except ValueError:
    print("I... I can't do this. You look way too nice today.")
finally:
    print("Anyway, thank you!")
