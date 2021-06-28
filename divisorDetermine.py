n = int(input("Enter the Number of apples: "))
min = int(input("Enter the minimum number: "))
max = int(input("Enter the maximum number: "))

# condition to get the divisor of numbers between minimum and maximum
if n>max and max>min:
    print("#The Divisor Determinator: \n")
    # minimum and maximum ranging
    for i in range(min,max+1):
        # conditioning of divisor
        if n%i==0:
            print(f"{i} is a divisor of {n}")
        else:
            print(f"{i} is not divisor of {n}")
# if max=min then only one number is there and it will be applicable for only one
elif max == min:
    if n % max == 0:
        print(f"{max} is a divisor of {n}")
    else:
        print(f"{max} is not divisor of {n}")
# otherwise invalid
else:
    print("You have put invalid number")