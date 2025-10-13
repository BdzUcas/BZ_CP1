#BZ 1st Password Strength Checker
#set password to input from user
password = input('Enter Password: ')
#set point value to 0
points = 0
#make a list of all special characters
special = '!@#$%^&*()_+-=[]{}|;:,.<>?'
#check if password is empty
if password.strip() == '':
    #do nothing
    pass
#otherwise
else:
    #if password contains a lowercase character
    for char in password:
        if char.islower():
            #add 1 point
            points += 1
            break
    #if password contains an uppercase character
    for char in password:
        if char.isupper():
            #add 1 point
            points += 1
            break
    #loop through each character of the password
    for char in password:
        #if current character is in the special characters list
        if char in special:
            #add one point
            points += 1
            #end loop early
            break
    #loop through each character of the password
    for char in password:
        #if current character is a number
        if char.isdigit():
            #add one point
            points += 1
            #end loop early
            break
    #if password length is greater than or equal to 8
    if len(password) >= 8:
        #add one point
        points += 1
    #if password length is greater than or equal to 10000
    if len(password) >= 10000:
        #add one point
        points += 1
#display point value/5
print(f'Strength Value: {points}/5')
#if point value is equal to 5
if points == 5:
    #display "Password Strength: Very Strong"
    print('Password Strength: Very Strong')
#if point value is equal to 4
elif points == 4:
    #display "Password Strength: Strong"
    print('Password Strength: Strong')
#if point value is equal to 3
elif points == 3:
    #display "Password Strength: Moderate"
    print('Password Strength: Moderate')
#if point value is equal to 2
elif points == 2:
    #display "Password Strength: Weak"
    print('Password Strength: Weak')
#if point value is equal to 1
elif points == 1:
    #display "Password Strength: Weak"
    print('Password Strength: Weak')
#if point value is less than 1
elif points < 1:
    #display "Password Strength: Probably already Comprimised"
    print('Password Strength: Probably Already Comprimised')
#otherwise
else:
    #display "Password Strength: ... ... ... What?"
    print('Password Strength: ... ... ... What?')