#BZ 1st *Args and **Kwargs Notes
#kwarguments
def say_hi(name = 'You',age= 'older than you look'):
    return f'Hi, {name} (age {age})!'

print(say_hi(name='Nathan',age=7))

def total(*numbers):
    return sum(numbers)

print(total(9,3,25))

def printValues(**kwarguments):
    for key in kwarguments.keys():
        print(f'{key}: {kwarguments[key]}')


printValues(name='james',age=17,cookie='oatmeal rasin')