# Checking if the number inputted is armstrong number or not
# while loop to continue till error
while True:
    n = int(input("Enter a number : "))
    sum = 0
    order = len(str(n))
    copy_n = n   #copying the number to check after the work is done

    # when number is greater than 0 continue the loop
    while(n>0):
        digit = n%10
        sum += digit**order
        n = n//10

    # when the number is same to the sum than it is armstrong number
    if (sum == copy_n):
        print(f"{copy_n} is an Armstrong number")
    else:
        print(f"{copy_n} is not an Armstrong number")