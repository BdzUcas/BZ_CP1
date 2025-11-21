#BZ 1st Factorial Calculator (Dirk's psuedocode, copied character for character)
#print(welcome to the factorial calculator! The factorial of a number is the number multiplied by every number below it, all the way to one. For example: The factorial of 5 is, 5*4*3*2*1=120)
print('welcome to the factorial calculator! The factorial of a number is the number multiplied by every number below it, all the way to one. For example: The factorial of 5 is, 5*4*3*2*1=120')
#define function factorial():
def factorial():
    #while True:
    while True:
        #factor = input(enter a full number)
        factor = input('enter a full number ')
        #if factor is an integer:
        if factor.isdigit():
            #(bracken insert): convert factor to integer
            factor = int(factor)
            #(bracken insert): make a copy of factor for use later (original_factor)
            original_factor = factor
            #break out of loop
            break
        #else:
        else:
            #print(please enter a valid input)
            print('please enter a valid input')

    #total = 1
    total = 1
    #num_down = 1
    num_down = 1
    #while factor > 0
    while factor > 0:
        #factor *= total (bracken's replacement): total *= factor
        total *= factor
        #factor -= num_down
        factor -= num_down

    #print(the answer is (total)) (bracken's replacement:) print(The original number was (original_factor). The answer is (total).)
    print(f'The original number was {original_factor}. The answer is {total}.')
#factorial()
factorial()