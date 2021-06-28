# Creating a Password Generator

# importing modules
import string
import random

# only applicable under this function
if __name__ == '__main__':
    while True:
        s1 = string.ascii_lowercase
        # print(s1)
        s2 = string.ascii_uppercase
        # print(s2)
        s3 = string.digits
        # print(s3)
        s4 = string.punctuation
        # print(s4)
        # input taking from the user for password length
        password_length = int(input("Enter Password length: \n"))
        # concatinating the string digits punctuation
        # making an empty list
        s = []
        # extending the empty list with the individual string, digit & punctuation
        s.extend(list(s1))
        s.extend(list(s2))
        s.extend(list(s3))
        s.extend(list(s4))
        # print(s)
        # # Method 1:
        # random.shuffle(s)
        # # print(s)
        # print("Your Password is : ",end="")
        # print("".join(s[0:password_length]))
        # Method 2
        print("Your Password is : ",end="")
        print("".join(random.sample(s,password_length)))