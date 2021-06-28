# Getting the execution time of a program
from time import time

# comparing both functions execution time

# function 1 to get execution time of it
def func1(a,b):
    pass

# function 2 to get execution time of it
def func2(a,b):
    num1 = a
    num2 = b
    if(a>b and a!=3):
        pass
    sum([4,3])
    return a+b

# only applicable when under these function
if __name__ == '__main__':
    # initializing time from here
    init = time()
    for i in range(1,1000000):
        func1(3,5)
    # function 1 execution time
    print("Function 1 execution time : ",time()-init)
    for i in range(1,1000000):
        func2(3,5)
    # function 2 execution time
    print("Function 2 execution time : ",time()-init)
    # overall execution time of the program
    print("Full Program execution time : ",time()-init)