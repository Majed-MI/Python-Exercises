# Factorial of a number
while(True):
    def factorial(n):
        # factorial syntax
        if n == 1:
            return 1
        else:
            return n*factorial(n-1)
    number = int (input("Enter a Number: "))
    # printing the factorial of the number
    print("The factorial of the number is:",factorial(number))

