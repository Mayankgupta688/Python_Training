7

7 * 6 * 5 * 4 * 3 * 2 * 1

def factorial(inputValue):

    if inputValue > 0:
        if inputValue == 1: 
            return 1
        else:
            return inputValue * factorial(inputValue - 1)
    else:
        raise Exception("Provide Positive Numbers")

print(factorial(3))