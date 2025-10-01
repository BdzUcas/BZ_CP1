#BZ 1st Multiplication Table
row = ''
for first_num in range(1,16):
    row = ''
    for second_num in range(1,16):
        num = str(first_num*second_num)
        if len(num) == 1:
            num = num + '  '
        elif len(num) == 2:
            num = num + ' '
        row = row + ' ' + num
    print(row)