if (9>0):
    print(True)
else:
    print(False)

if (9>0) and (5>6):
    print("Second True")
elif True and not False:
    print("elif true")
else:
    print("Second False")
 
# code fo a basic calculator

    num1 = float(input("Enter first number : "))
    optr = str(input("Enter the operator : "))
    num2 = float(input("Enter second number : "))
    flag = 1

    if optr == '+':
        res = num1 + num2
    elif optr == '-':
        res = num1 - num2
    elif optr == '*':
        res = num1 * num2
    elif optr == '/':
        res = num1 / num2
    else:
        flag = 0;
        print("Illegal operation");

    if flag != 0:
        print(res)