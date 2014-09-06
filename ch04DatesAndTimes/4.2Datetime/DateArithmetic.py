#!/usr/bin/env python3

import datetime

today = datetime.date.today()
one_day = datetime.timedelta(days=1)
yesterday = today - one_day
tomorrow = today + one_day

print('Today:', today)
print('Yesterday:', yesterday)
print('Tomorrow:', tomorrow)

print(tomorrow - yesterday)
print(yesterday - tomorrow)
