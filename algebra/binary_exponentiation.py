def binaryExponentiation_recursion(a, b):
    if(b == 0):
        return 1
    res = binaryExponentiation_recursion(a, b//2)
    if(b%2 == 0):
        return res*res
    else:
        return res*res*a


def binaryExponentiation_iterative(a, b):
    result = 1
    while(b>0):
        if(b&1 == 1):
            result = result*a
        a = a*a
        b = b >> 1
    return result

print(binaryExponentiation_iterative(3, 7))
print(binaryExponentiation_recursion(3, 7))