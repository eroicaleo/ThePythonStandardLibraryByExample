#!/usr/bin/env python3

import hashlib
import time

data = open(__file__, 'rt').read()
for i in range(5):
    h = hashlib.sha1()
    print(time.ctime(), '%0.3f %0.3f' % (time.time(), time.clock()))
    for i in range(30000):
        h.update(data.encode('utf-8'))
    cksum = h.digest()

for i in range(6, 1, -1):
    print('%s %0.2f %0.2f' % (time.ctime(), time.time(), time.clock()))
    print('Sleeping', i)
    time.sleep(i)
