#!/usr/bin/env python3

import datetime
import time

def show_struct(s):
    print (' tm_year :', s.tm_year)
    print (' tm_mon  :', s.tm_mon)
    print (' tm_mday :', s.tm_mday)
    print (' tm_hour :', s.tm_hour)
    print (' tm_min  :', s.tm_min)
    print (' tm_sec  :', s.tm_sec)
    print (' tm_wday :', s.tm_wday)
    print (' tm_yday :', s.tm_yday)
    print (' tm_isdst:', s.tm_isdst)

today = datetime.date.today()
print(today)
print(today.ctime())

tt = today.timetuple()
show_struct(tt)
print (' ordinal :', today.toordinal())
print (' year    :', today.year)
print (' month   :', today.month)
print (' day     :', today.day)

o = 733114
print('o            :', o)
print('fromordinal  :', datetime.date.fromordinal(o))
t = time.time()
print('t            :', t)
print('fromtimestamp:', datetime.date.fromtimestamp(t))

print('Earliest  :', datetime.date.min)
print('Latest    :', datetime.date.max)
print('Resolution:', datetime.date.resolution)

d1 = datetime.date(2012, 12, 28)
print('The day shannon born:', d1)
d2 = d1.replace(year=2013)
print('Shannon\'s first birthday:', d2)
