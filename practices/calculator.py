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
    num1 = input('> ').strip()
    if num1.replace('.','').isdigit():
        num1 = float(num1)
        break
    else:
        print('Invalid number')
while True:
    print('Enter second number')
    num2 = input('> ').strip()
    if num2.replace('.','').isdigit():
        num2 = float(num2)
        break
    else:
        print('Invalid number')
if operator == '+':
    output = num1+num2
if operator == '-':
    output = num1-num2
if operator == '*':
    output = num1*num2
if operator == '/':
    output = num1/num2
if operator == '%':
    output = num1%num2
if operator == '**':
    output = num1**num2
if operator == '//':
    output = num1//num2
print(f'{num1:.2f} {operator} {num2:.2f} = {output:.2f}')