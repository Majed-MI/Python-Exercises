print("Enter the numbers of the list one by one \n")
#taking the size of the list
size = int(input("Enter the size of the list\n"))
# initializing an empty list
mylist = []
# taking list element one by one
for i in range (size):
    mylist.append(int(input("Enter list element:")))

# printing original list
print(f"Your list is {mylist}")

# Reversing process
reverse = mylist[::-1]
print(f"Your list is reversed. Now the list looks like {reverse}")