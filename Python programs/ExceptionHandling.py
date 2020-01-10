
# Exception handling in Python

try:
    number = int(input("Enter a number : "))
    num = 10/0
    print(number)

except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("ValueError")
