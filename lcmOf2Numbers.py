# Finding lcm of 2 numbers
while True:
    a = int(input("Enter First Number : "))
    b = int(input("Enter Second Number : "))

    # declaring max of the 2 input numbers
    maxNum = max(a,b)

    # if one number is the lcm of the other number then it will be printed
    while True:
        # when the remainder of two numbers are 0 then the number will be lcm
        if(maxNum%a == 0 and maxNum%b == 0):
            break           #Break the loop when it is done
        maxNum = maxNum + 1         #incrementing the maxNum if not found lcm
    
    print(f"The lcm of {a} and {b} is : {maxNum}")