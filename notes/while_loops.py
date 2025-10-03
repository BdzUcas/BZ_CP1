#BZ 1st While Loops Notes
import random
import time
years = 0
while years < 20:
    years += 1
    if input('Break Out? Y/N: ').strip().lower() == 'y':
        break
    else:
        print(f'{20 - years} years left in prison ')
    time.sleep(1)
else:
    print('You served your sentence and can now reintegrate into society!')
if years < 20:
    print('You broke out and are now a fugitive from the law')