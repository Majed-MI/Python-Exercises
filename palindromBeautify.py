# Palindrome P  rogram Beautify

from time import time
# function for the palindrome determination
def next_palindrome(n):
    # condition for n greater than 10 working
    if n > 10:
        # plus one adding to the integer number to find the palindrome number
        n = n + 1
        # while loop to continue the loop again and again to get the palindrome number
        while not is_palindrome(n):
            # when not palindrome adding 1 more and checking the next one
            n += 1
        # if palindrome then the loop will end
        # returning the value again in the function and adding more to check
        return n

    # condition for less than 10
    else:
        return f"{n} : It is less than 10"


# function for palindrome checking
def is_palindrome(n):
    # return if the palindrome condition matching is found
    return str(n) == str(n)[::-1]


# only applicable in these main function
if __name__ == '__main__':
    init = time()
    print("--Welcome to the Next Palindrome Program--")
    # How many number you want to test
    a = int(input("--Please enter number of test cases\n"))
    # blank list for the numbers
    n = []

    # range for test cases to for loops continue
    for i in range(a):
        # taking the number in integer
        item = int(input("Enter a Number:\n"))
        # adding the number in the list of number
        n.append(item)
    # for the range in test case a, printing the number serially and the palindrome number will be the
    # function working value
    for i in range(a):
        print(f"Next Palindrome for {n[i]} is {next_palindrome(n[i])}")

    print("Overall execution time is : ",time()-init)
