# a+b*c/d calculator
def add(a, b):
    return a+b

def sub(a, b):
    return a-b

def mul (a, b):
    return a*b

def div (a, b):
    return a/b

a = int(input ("input a = "))
b = int(input ("input b = "))
c = int(input ("input c = "))
d = int(input ("input d = "))

def calculator (a, b, c, d):
    print (a+b*c/d)

calculator(a, b, c, d)