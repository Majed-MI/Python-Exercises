# Star Pattern forward and reverse
# continuing the loop through while
while(True):
    print("How many row?")
    # one is the row counter
    one = int(input())
    print("Type 1 or 0")
    # two is the forward or reverse indicator through boolean
    two = int(input())
    new = bool(two)
    # For forward
    if new == True:
        for i in range(1,one+1):
            for j in range(1,i+1):
                print("*",end=" ")
            print()
    # For Reverse
    elif new == False:
        for i in range(one,0,-1):
            for j in range(1,i+1):
                print("*",end=" ")
            print()