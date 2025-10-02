#BZ 1st Multiplication Table
row = ''
while True:
    size = input('Input Size: ')
    if size.isdigit():
        size = int(size) + 1
        break
    else:
        print('Please input a number!')
for i in range(1,size):
        num = str(i)
        if len(num) == 1:
            num = num + '  '
        elif len(num) == 2:
            num = num + ' '
        row = row + ' ' + num
print('     '+row+'\n')
for first_num in range(1,size):
    row = ''
    for second_num in range(1,size):
        num = str(first_num*second_num)
        if len(num) == 1:
            num = num + '  '
        elif len(num) == 2:
            num = num + ' '
        row = row + ' ' + num
    start = str(first_num)
    if len(start) == 1:
        print(start + '    ' + row)
    elif len(start) == 2:
        print(start + '  ', row)
    else:
        print(start + ' ', row)