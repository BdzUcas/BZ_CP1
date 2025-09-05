#BZ 1st Idiot Proof
def validate_name(name):
    name = name.strip().lower()
    if not name.count(' ') == 1:
        return False
    first_name, last_name = name.split(' ')
    if len(first_name) == 0 or len(last_name) == 0:
        return False
    name = first_name.capitalize() + ' ' + last_name.capitalize()
    return name

def validate_number(number):
    number = number.strip().replace(' ', '').replace('-', '')
    if not number.isdigit():
        return False
    if not len(number) == 10:
        return False
    number = f'{number[:3]} {number[3:6]} {number[6:]}'
    return number

def validate_gpa(gpa):
    if not gpa.replace('.', '').isdigit():
        return False
    gpa = float(gpa.strip().replace(' ', ''))
    if gpa > 4:
        return False
    return gpa

while True:
    name = input('Enter your first and last name: ')
    if not validate_name(name) == False:
        name = validate_name(name)
        print(f'Your name is {name}')
        break
    else:
        print('invalid name!')

while True:
    phone_number = input('Enter your phone number: ')
    if not validate_number(phone_number) == False:
        phone_number = validate_number(phone_number)
        print(f'Your number is {phone_number}')
        break
    else:
        print('invalid number!')

while True:
    gpa = input('Enter your GPA: ')
    if not validate_gpa(gpa) == False:
        gpa = validate_gpa(gpa)
        print(f'Your GPA is {gpa}')
        break
    else:
        print('invalid GPA!')

print(f'information: name {name}, phone number {phone_number}, gpa {gpa}')
