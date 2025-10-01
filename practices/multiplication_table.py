#BZ 1st Multiplication Table
row = ''
while True:
    size = input('Input Size: ')
    if size.isdigit():
        size = int(size) + 1
        break
    else:
        print('Please input a number!')
for first_num in range(1,size):
    row = ''
    for second_num in range(1,size):
        num = str(first_num*second_num)
        if len(num) == 1:
            num = num + '  '
        elif len(num) == 2:
            num = num + ' '
        row = row + ' ' + num
    print(row)