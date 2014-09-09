#!/usr/bin/env python3

import datetime

print('microseconds:', datetime.timedelta(microseconds=1))
print('milliseconds:', datetime.timedelta(milliseconds=1))
print('seconds     :', datetime.timedelta(seconds=1))
print('minutes     :', datetime.timedelta(minutes=1))
print('hours       :', datetime.timedelta(hours=1))
print('days        :', datetime.timedelta(days=1))
print('weeks       :', datetime.timedelta(weeks=1))

for delta in [
datetime.timedelta(microseconds=1),
datetime.timedelta(milliseconds=1),
datetime.timedelta(seconds=1),
datetime.timedelta(minutes=1),
datetime.timedelta(hours=1),
datetime.timedelta(days=1),
datetime.timedelta(weeks=1),
]:
    print('Total:', delta.total_seconds())
