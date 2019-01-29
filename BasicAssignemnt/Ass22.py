# Python program to find the H.C.F of two input number
num1=input("enter first number:")
num2=input("second number:")

def calculateHCF(x, y):
    # choose the smaller number
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller + 1):
        if ((x % i == 0) and (y % i == 0)):
            hcf = i

    return hcf



print("The H.C.F. of", num1, "and", num2, "is", calculateHCF(num1, num2))