# factorial and number of trailing zeros

# Factorial function
def factorial(number):
    if number == 1:
        return 1
    elif number < 1:
        return "Enter a Positive number Please"
    else:
        return number * factorial(number-1)

# factorial trailing zero  which finds how many zeroes is there in the factorial
def factorialTrailingZeros(number):
    fac = factorial(number)
    count = 0
    i = 5
    while(number//i != 0):
        count += int(number/i)
        i=i*5
    return count

# only applicable when under these function
if __name__ == '__main__':
    while True:
        number = int(input("Enter a Number : "))
        fac = factorial(number)
        print(f"The Factorial of {number} is : {fac}")
        zero = factorialTrailingZeros(number)
        print(f"The trailing zeros in this factorial is {zero}")