def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    return a / b

def main():
    num1 = float(input("1 - son: "))
    num2 = float(input("2 - son: "))
    op = input("Amal: ")

    if op == '+':
        print(add(num1,num2))
    elif op == '-':
        print(subtract(num1,num2))
    elif op == '*':
        print(multiply(num1,num2))
    elif op == '/':
        print(divide(num1,num2))
    else:
        print('Bunday amal yoq')

main()