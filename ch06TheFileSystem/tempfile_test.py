#!/usr/bin/env python3

import os
import tempfile

print('Building a file with PID:')
filename = '/tmp/guess_my_name.%s.txt' % (os.getpid())
print(filename)
temp = open(filename, 'w+b')
try:
    print('temp:')
    print('  ', temp)
    print('temp.name:')
    print('  ', temp.name)
finally:
    temp.close()
    os.remove(filename)

print()

print('TemporaryFile:')
temp = tempfile.TemporaryFile()
try:
    print('temp:')
    print('  ', temp)
    print('temp.name:')
    print('  ', temp.name)
finally:
    temp.close()

with tempfile.TemporaryFile() as temp1:
    temp1.write(bytes('Some Data', 'UTF-8'))
    temp1.seek(0)
    print(temp1.read())

with tempfile.TemporaryFile(mode='w+t') as temp1:
    temp1.writelines(['first\n', 'second\n'])
    temp1.seek(0)
    for line in temp1:
        print(line.rstrip())

with tempfile.NamedTemporaryFile() as temp:
    print('temp:')
    print('  ', temp)
    print('temp.name:')
    print('  ', temp.name)

print("Exists after close:", os.path.exists(temp.name))

directory_name = tempfile.mkdtemp()
print(directory_name)
os.removedirs(directory_name)

with tempfile.NamedTemporaryFile(
        prefix='prefix_',
        suffix='_suffix',
        dir='/tmp') as temp:
    print('temp:')
    print('  ', temp)
    print('temp.name:')
    print('  ', temp.name)


print("tempfile.gettempdir():", tempfile.gettempdir())
print("tempfile.gettempprefix():", tempfile.gettempprefix())

tempfile.tempdir = '/Ge/Shannon/Melon/Xiangxiang'

print("tempfile.gettempdir():", tempfile.gettempdir())
print("tempfile.gettempprefix():", tempfile.gettempprefix())
