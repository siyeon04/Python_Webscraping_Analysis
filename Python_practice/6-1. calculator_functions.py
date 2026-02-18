def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

num1, num2 = 10, 5

print(f"{num1} + {num2} = {add(num1, num2)}")
print(f"{num1} - {num2} = {sub(num1, num2)}")
print(f"{num1} * {num2} = {mul(num1, num2)}")
print(f"{num1} / {num2} = {div(num1, num2)}")