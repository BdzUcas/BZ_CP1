#BZ 1st Password Strength Checker
#set password to input from user
password = input('Enter Password: ')
#set point value to 0
points = 0
#make a list of all special characters
special = '!@#$%^&*()_+-=[]{}|;:,.<>?'
#if password is not all lowercase
    #add 1 point
#if password is not all uppercase
    #add 1 point
#loop through each character of the password
    #if current character is in the special characters list
        #add one point
        #end loop early
#loop through each character of the password
    #if current character is a number
        #add one point
        #end loop early
#if password length is greater than or equal to 8
    #add one point
#display point value/5
#if point value is equal to 5
    #display "Password Strength: Very Strong"
#if point value is equal to 4
    #display "Password Strength: Strong"
#if point value is equal to 3
    #display "Password Strength: Moderate"
#if point value is equal to 2
    #display "Password Strength: Weak"
#if point value is equal to 1
    #display "Password Strength: Weak"
#if point value is less than 1
    #display "Password Strength: Probably Already Comprimised"
#otherwise
    #display "Password Strength: ... ... ... What?"