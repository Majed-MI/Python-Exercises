# 45*3 = 555; 56+9 = 77; 56/6 = 4;
# These are the error which will occur in these program and rest expressions maths will be OK!
#continuing the loop again and again until wrong input given
while(True):
    print("Enter the First Number: ")
    num1 = int (input())
    print("Enter the Second Number: ")
    num2 = int (input())
    print("Enter the Operator: (+,-,*,/,%) ")
    oper = input()
    # faulty error
    if(num1 == 45 and num2 == 3 and oper == '*'):
        print("555")
    # faulty error
    elif(num1 == 56 and num2 == 9 and oper == '+'):
        print("77")
    # faulty error
    elif (num1 == 56 and num2 == 6 and oper == '/'):
        print("4")
    # + operations
    elif (oper == '+'):
        addition = num1 + num2
        print(addition)
    # - operations
    elif (oper == '-'):
        subtraction = num1 - num2
        print(subtraction)
    # * operations
    elif (oper == '*'):
        multiplication = num1 * num2
        print(multiplication)
    # / operations
    elif (oper == '/'):
        division = num1 / num2
        print(division)
    # % operations
    elif (oper == '%'):
        modulus = num1 % num2
        print(modulus)
    # invalid operator
    else:
        print("Error! Please Check Again")