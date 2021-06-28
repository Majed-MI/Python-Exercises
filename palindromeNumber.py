# Palindrome Number Determination
# while loop for continuing again and again
while True:
    print("Enter your number : ")
    number = int(input())
    # storing the number to temp
    temp = number
    # declaring reverse to 0
    reverse = 0

    # applicable till the number is positive
    while (number>0):
        digit = number % 10      #getting the last digit of the number as modulus
        reverse = reverse * 10 + digit     #getting the last digit as reverse
        number = number//10         #knocking out the last digit of the number and continuing

    # when the number is same as reverse then it is palindrome
    if temp == reverse:
        print(f"{temp} is a Palindrome Number")
    # otherwise not palindrome
    else:
        print(f"{temp} is not a palindrome number")