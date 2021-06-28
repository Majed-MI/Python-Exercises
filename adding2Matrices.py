# Adding 2 matrics in python

# function to take input for the matrics i,j
def matrix(m,n):
    # declaring o as an empty list to take input from the user for matrics
    o = []
    # for the rows
    for i in range(m):
        # declaring row as an empty list to take the row from the user input
        row = []
        # for the columns
        for j in range(n):
            inp = int(input(f"Enter O[{i}] [{j}]: "))
            # input appending to the list of row which is a matrics
            row.append(inp)
        # and finally full row and column one by one is added to the o list
        o.append(row)
    # returning o to make further work with it
    return o

# sum function to add the 2 matrics
def sum(A,B):
    # declaring output as the empty list which is addition of the two matrics which will be later included
    output = []
    for i in range(len(A)):         #Number of rows
        row = []
        for j in range(len(A[0])):      #Number of columns
            # appending the multiplication in the row list
            row.append(A[i][j] + B[i][j])
        # appending the list output which is the final addition
        output.append(row)
    return output

# input taking from the user to determine row & column
m = int(input("Enter the value of m : \n"))
n = int(input("Enter the value of n : \n"))
print("Enter Matrix A")
A = matrix(m,n)
print("Enter Matrix B")
B = matrix(m,n)
# print(A)
# addition of the function sum
s = sum(A,B)
print(s)