# code to find exponent of number

def power(num,pow):
    res = 1
    for index in range(pow):
        res *= num
    return res

print(power(2,3))



