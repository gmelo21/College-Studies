# Nov 4, 2024.

# Working with recursive functions! First project in a few weeks, after I went through a pretty big burnout from actual coding.
# Happens to the best of us. Most importantly, I think I understood why it happened and how to deal with it, too. So y'all can 
# bet I'll continue to come back stronger than ever, over and over again!

# To all of our displeasure, I couldn't think of any quirky project to do that used recursiveness, so take the 
# exercises we are given in class instead. It's just one of those things you just have to make-do. 


# Sum of all elements of a list:

def list_sum(chosenList):
    if len(chosenList) == 1:
        return chosenList[0]
    else:
        return chosenList[0] + list_sum(chosenList[1::])
    
    
yourList = []
yourLength = int(input("Choose the desired length for your lists: (Keep it short. Wastes less time for you and it makes the code easier to check!) "))

for i in range(0, yourLength):
    yourNumber = float(input(f"({i + 1}/{yourLength}) Choose a number to be added to your list: "))
    yourList.append(yourNumber)
    
print(f"The sum of all numbers inside the list is: {list_sum(yourList)}")
print()


# Sum of numbers from 0 to N:

def number_sum(chosenNumber):
    if chosenNumber == 1:
        return 1
    else:
        return chosenNumber + number_sum(chosenNumber - 1)
    
    
yourNumber = float(input(f"Choose a number: "))
    
print(f"The sum of the numbers from 0 to your number ({yourNumber}) is: {number_sum(yourNumber)}")
print()


# GCD of two numbers.

def gcd_calculator(x, y):
    if x >= y and x % y == 0:
        return y
    elif x < y:
        return gcd_calculator(y, x)
    else:
        return gcd_calculator(y, x % y)


yourX = int(input('X\'s value: '))
yourY = int(input('Y\'s value: '))
print(f"The GCD of {yourX} and {yourY} is: {gcd_calculator(yourX, yourY)}")
print()

