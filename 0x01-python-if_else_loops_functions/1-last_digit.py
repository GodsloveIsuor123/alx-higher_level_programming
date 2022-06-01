#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    extra = number % -10
else:
    extra = number % 10
print('Last digit of', number, 'is', extra, end=' ')
if extra > 5:
    print('and is greater than 5')
elif extra == 0:
    print('and is 0')
else:
    print('and is less than 6 and not 0')
