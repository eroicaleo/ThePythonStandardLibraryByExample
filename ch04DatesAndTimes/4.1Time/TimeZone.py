#!/usr/bin/env python3

import os
import time

def show_zone_info():
    print('TZ        :', os.environ.get('TZ', '(not set)'))
    print('tzone name:', time.tzname)
    print('Zone      : %d (%d)' % (time.timezone, time.timezone/3600))
    print('DST       :', time.daylight)
    print('time      :', time.ctime())

print('Default:')
show_zone_info()

ZONES = ['GMT', 'Europe/Amsterdam']

for zone in ZONES:
    os.environ['TZ'] = zone
    time.tzset()
    print(zone, ':')
    show_zone_info()
