# Finding HCF or GCD of 2 Numbers
while True:
    num1 = int(input("Enter first Number : "))
    num2 = int(input("Enter second Number : "))

    # condition to find the minimum number between the two
    if num2>num1:
        min = num1

    else:
        min = num2

    # the condition for gcd when the two numbers both are divisible by a minimum number
    for i in range(1,min+1):
        if (num1%i == 0 and num2%i == 0):
            hcf = i

    print(f"The HCF/GCD of {num1} and {num2} is {hcf}")

