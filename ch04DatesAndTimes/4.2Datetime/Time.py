#!/usr/bin/env python3

import datetime

t = datetime.time(1, 2, 3)
print(t)
print('hour       :', t.hour)
print('minute     :', t.minute)
print('second     :', t.second)
print('microsecond:', t.microsecond)
print('time zone  :', t.tzinfo)

print('Earliest   :', t.min)
print('latest     :', t.max)
print('Resolution :', t.resolution)

for m in [0, 1, 0.1, 0.6]:
    try:
        print('%.2f' % m, datetime.time(0, 0, m))
    except TypeError as err:
        print('Error:', err)
