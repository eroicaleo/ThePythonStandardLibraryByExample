#!/usr/bin/env python3

import time

print('The time is:        ', time.time())
print('The time is:        ', time.ctime())
print('15 seconds from now:', time.ctime(time.time()+15))
