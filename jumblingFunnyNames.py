# Jumbling Funny Names with random modules
import random
num = int(input("How many Name you want to give?"))
# declaring an empty name list to append from the input given by user
name_list = []

# for the range of the number checking
for i in range(num):
    # taking name input and printing through f string one by one serially
    name_input = input(f"Name{i+1} : ")
    # appending the name in the list
    name_list.append(name_input)

# declaring first name and last name as an empty list
first_name = []
last_name = []

# for item in the list of the name the function will work
for name in name_list:
    # splitting the name through a space and ignoring more space by strip()
    # separating the first word in a and last word in b
    a,b = name.strip().split(' ')
    # appending first name from a and last name from b
    first_name.append(a)
    last_name.append(b)

# declaring an empty random list
random_list = []
# while loop till any error
while True:
    # if the first word is not empty and also the last word then this function will work
    if(len(first_name)!=0 and len(last_name)!=0):
        # declaring random a and random b which will be randomly filled up by the random choice of the
        # first names list and last names list
        random_a = random.choice(first_name)
        random_b = random.choice(last_name)
        # appending the random list from the choice random
        random_list.append(random_a+" "+random_b)
        # after the storing in the list is done removing the random choice and re running the loop
        first_name.remove(random_a)
        last_name.remove(random_b)

    # if the first and last words are emty then break the loop
    else:
        break

# for item in the randomlist print the items from the list randomlist
for fun in random_list:
    print(f"Funny Name: {fun}")