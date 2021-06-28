# Fake multiplication table catch error
import random

# function for the rayed wrong multiplication table and taking the value number input
def rayedMultipleTable(number):
    # generating a wrong number between 1 to 8
    wrong = random.randint(1,9)
    # table declaring var to table calculation in one line
    table = [ i*number for i in range(1,11)]
    # anyone number will be wrong and wrong multiply will occur
    table[wrong] = table[wrong] + random.randint(1, 5)
    # return the table so when function is called it is print
    return table

# validation function taking two value one table and the other number
def validationTable(table,number):
    for i in range(1,11):
        # if any multiplication is error try catching it
        if table[i-1] != number*i:
            # printing the index no.
            print(f"The wrong index is at {i-1}")
            # printing the result which should be
            print(f"The correct answer should be {number*i}")
    # return nothing
    return ""

# only applicable when under these function
if __name__ == '__main__':
    # try to do these when the user inputs integer otherwise except will handle error
    try:
        number = int(input("Enter a Number for multiplication: "))
        # calling function of rayed and the input number is the value of the function
        rayed = rayedMultipleTable(number)
        print(rayed)
        # wrongindex is the function calling
        wrongIndex = validationTable(rayed,number)
        print(wrongIndex)
    # catch the error
    except Exception as e:
        print("Please enter a valid input")


