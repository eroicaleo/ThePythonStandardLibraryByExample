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

print("########## copy ##############")
import os.path
if not os.path.isdir('example'):
    os.mkdir('example')
else:
    print('example already exists!')

print('BEFORE:')
print(os.listdir('example'))
copy('shutil_test.py', 'example')
print('AFTER:')
print(os.listdir('example'))
os.unlink('example/shutil_test.py')

import time

def show_file_info(filename):
    stat_info = os.stat(filename)
    print('\tMode:', stat_info.st_mode)
    print('\tCreated:', time.ctime(stat_info.st_ctime))
    print('\tAccessed:', time.ctime(stat_info.st_atime))
    print('\tModified:', time.ctime(stat_info.st_mtime))

print('SOURCE:')
show_file_info(__file__)
print('DEST:')
copy2(__file__, 'example')
show_file_info('example/shutil_test.py')
os.unlink('example/shutil_test.py')

print("########## copymode ##############")
