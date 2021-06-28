# Securing password of any string word or something

# declaring the data to change when the letter or word is similar to the same
SECURE = (('s','$'),('and','&'),('a','@'),('i','!'),('o','0'))

# securing Password function
def securePassword(password):
    # for the tuple of SECURE replace the data
    for a,b in SECURE:
        password = password.replace(a,b)
    return password

# only applicable under this function
if __name__ == '__main__':
    password = input("Enter your password : ")
    password = securePassword(password)   #Calling back the function
    print(f"Your secure password is : {password}")
