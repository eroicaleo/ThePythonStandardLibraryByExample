#!/usr/bin/env python3

from shutil import *
from glob import glob
import os
import sys
from io import StringIO

print("########## copyfile ##############")
print('BEFORE:', glob('shutil_test*'))
copyfile('shutil_test.py', 'shutil_test.py.copy')
print('BEFORE:', glob('shutil_test*'))

print("########## copyfileobj ##############")

class VerboseStringIO(StringIO):
    def read(self, n=-1):
        next = StringIO.read(self, n)
        print('read (%d) bytes' % n)
        return next

lorem_ipsum = '''Lorem ipsum dolor sit amet, consectetuer adipiscing
elit. Vestibulum aliquam mollis dolor. Donec vulputate nunc ut diam.
Ut rutrum mi vel sem. Vestibulum ante ipsum.'''

print('DEFAULT:')
input = VerboseStringIO(lorem_ipsum)
output = StringIO()
copyfileobj(input, output)
print(output.getvalue())

print('All at once:')
input = VerboseStringIO(lorem_ipsum)
output = StringIO()
copyfileobj(input, output, -1)

print('Block at 256')
input = VerboseStringIO(lorem_ipsum)
output = StringIO()
copyfileobj(input, output, 256)
