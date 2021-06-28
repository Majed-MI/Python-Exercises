# if number is greater than 100 loops close
while(True):
    inp = int (input("Enter a Number: "))
    # number>100 breaks the loops
    if (inp > 100):
        print("Congrats! You have entered more than 100 & the loop stops here! ")
        break
    # otherwise continue
    else:
        print("Try Again! Enter number greater than 100 to end the loop")
        continue
