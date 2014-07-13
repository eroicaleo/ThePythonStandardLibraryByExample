#!/usr/bin/env python3

import os
import linecache
import tempfile

lorem = '''Lorem ipsum dolor sit amet, consectetuer
adipiscing elit. Vivamus eget elit. In posuere mi non
risus. Mauris id quam posuere lectus sollicitudin
varius. Praesent at mi. Nunc eu velit. Sed augue massa,
fermentum id, nonummy a, nonummy sit amet, ligula. Curabitur
eros pede, egestas at, ultricies ac, apellentesque eu,
tellus.

Sed sed odio sed mi luctus mollis. Integer et nulla ac augue
convallis accumsan. Ut felis. Donec lectus sapien, elementum
nec, condimentum ac, interdum non, tellus. Aenean viverra,
mauris vehicula semper porttitor, ipsum odio consectetuer
lorem, ac imperdiet eros odio a sapien. Nulla mauris tellus,
aliquam non, egestas a, nonummy et, erat. Vivamus sagittis
porttitor eros.'''

def makefile():
    fd, temp_file_name = tempfile.mkstemp()
    os.close(fd)
    fd = open(temp_file_name, 'wt')
    try:
        fd.write(lorem)
    finally:
        fd.close()
    return temp_file_name

def cleanup(filename):
    os.unlink(filename)

filename = makefile()

print('SOURCE:')
print('%r' % (lorem.split('\n')[4]))
print()
print('CACHE:')
print('%r' % linecache.getline(filename, 5))
print()
print('BLANK: %r' % linecache.getline(filename, 8))
print()

not_there = linecache.getline(filename, 500)
print('NOT THERE: %r includes %d characters' % (not_there, len(not_there)))

module_line = linecache.getline('linecache.py', 3)
print('MODULE:')
print(repr(module_line))

file_src = linecache.__file__
if file_src.endswith('.pyc'):
    file_src = file_src[:-1]
print('\nFILE:')
with open(file_src, 'r') as f:
    file_line = f.readlines()[2]
print(file_line)
