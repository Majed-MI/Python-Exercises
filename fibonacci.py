# fibonacci series
while(True):
    def fibonacci(n):
            # fibonacci syntax
            if n <= 1:
                return n
            else:
                return fibonacci(n-1) + fibonacci(n-2)
    # number to which will show the series
    number = int (input("Enter the number to print till that fibonacci series: "))

    # invalid error handling
    if number<=0:
        print("Please Enter a positive Integer")
    # fibonacci series serially printing
    else:
        print("Fibonacci Sequence: ")
        for i in range (number):
            print(fibonacci(i),end=" " )
    print("\n")