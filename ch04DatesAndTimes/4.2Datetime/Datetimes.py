#!/usr/bin/env python3

import datetime

print('now   :', datetime.datetime.now())
print('today :', datetime.datetime.today())
print('utcnow:', datetime.datetime.utcnow())

d = datetime.datetime.now()
FIELDS = ['year', 'month', 'day', 'hour', 'minute', 'second', 'microsecond']
for f in FIELDS:
    print('%15s : %s' % (f, getattr(d, f)))

t = datetime.time(1, 2, 3)
print('t:', t)
d = datetime.date.today()
print('d:', d)
dt = datetime.datetime.combine(d, t)
print('dt:', dt)
