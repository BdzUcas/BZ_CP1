#BZ 1st Basic Calculator
valid_ops = ['+','-','*','/','%','**','//']
while True:
    print('Enter operation to run: + for addition, - for subtraction, * for multiplication, / for division, % for modulus, ** for exponents, or // for integer division')
    operator = input('> ').strip()
    if operator in valid_ops:
        break
    else:
        print('Invalid operator')
while True:
    print('Enter first number')
    num1 = input('> ')
    if num1.isdigit():
        num1 = int(num1)
        break
    else:
        print('Invalid number')
while True:
    print('Enter second number')
    num2 = input('> ')
    if num2.isdigit():
        num2 = int(num2)
        break
    else:
        print('Invalid number')