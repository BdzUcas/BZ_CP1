#BZ 1st Booleans
import time
import datetime as date
import random
cur_time = time.time()
legible_time = time.ctime(cur_time)
print(f'Seconds since 1970 {cur_time}')
print(f'Actually readable: {legible_time}')
bettah_time = date.datetime.now()
hour = bettah_time.strftime('%h')
print(f'just the hour: {hour}')
print(f'The hour is saved as an integer: {isinstance(hour, int)}')
print(f'The hour is saved as an float: {isinstance(hour, float)}')
print(f'The hour is saved as an boolean: {isinstance(hour, bool)}')
print(f'The hour is saved as an string: {isinstance(hour, str)}')

print(f'current datetime time {bettah_time}')
printer = ''
# minutes = %M
# weekday = %A %a
# day = %d
# month = %B %b
# month number = %m
# year = %Y %y
# seconds %S

print(bool(' '))
to_print = input('what to print? ')
for i in to_print:
    printer = printer + i
    print(printer)
    time.sleep(0.1)
printer = ''
for i in range (0,100):
    printer = printer + str(random.randint(0,9))
print(float(printer)/time.time())