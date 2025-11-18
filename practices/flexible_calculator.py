#BZ 1st Flexible Calculator Calculator
#operation function
def run_operation(numbers,op):
    #if our operation is max
    if op == 'max':
        #return max of numbers
        return max(numbers)
    #if our operation is min
    elif op == 'min':
        #return min of numbers
        return min(numbers)
    #if our operation is sum, average or product
    elif op in ['sum','average','product']:
        #create sum variable and set it equal to 0
        sum = 0
        #loop through list of numbers
        for number in numbers:
            #if operation is sum or average
            if op in ['sum','average']:
                #add current number to sum
                sum += number
            #if operation is product
            elif op == 'product':
                #if sum is 0
                if sum == 0:
                    #set sum to 1
                    sum = 1
                #mutliply sum by number
                sum *= number
        #if operation is average
        if op == 'average':
            #divide sum by length of numbers list
            sum /= len(numbers)
        #return sum
        return sum
    #if our operation is anything else
    else:
        #return error
        return 'Invalid Operation'
#welcome user to program
print('Welcome to the Flexible Calculator!')
#forever
while not False:
    #ask what operation they want to use
    operation = input('What operation? Max, Min, Sum, Average, and Product are available.\n').lower()
    #if it is a valid operation
    if operation in ['max','min','sum','average','product']:
        #end loop
        break
    #otherwise
    else:
        #tell user to select a valid operation
        print('Please select a valid operation!  Max, Min, Sum, Average, and Product are available.')
#prompt user to enter a number or "done" to be done
print('Enter a number or enter "done" to finish.')
#create empty numbers list
nums = []
#forever
while not False:
    #take input from user
    num_in = input('> ').strip().lower()
    #if input is a number
    try:
        num_in = float(num_in)
        #add it to numbers list
        nums.append(num_in)
    except:   
        #otherwise if input is "done":
        if num_in in ['done','end','over','exit','break']:
            #end loop
            break
        #otherwise
        else:
            #tell user to enter numbers or "done"
            print('Please enter a number or "done".')
#run operation on numbers list
print(f'Result: {run_operation(numbers = nums,op = operation)}')
#the generator wasn't passing arguments but instead just the generator object as an argument and i wasn't sure how to fix that so i just passed it as a list sorry