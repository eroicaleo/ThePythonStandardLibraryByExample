#!/usr/bin/env python3

import os
import os.path
import time

print("os.path.sep:", os.path.sep)

print('######### os.path.split ###########')

for path in ['/one/two/three',
        '/one/two/three/',
        '/',
        '.',
        '']:
    print('%15s : %s' % (path, os.path.split(path)))

print('######### os.path.basename ###########')

for path in ['/one/two/three',
        '/one/two/three/',
        '/',
        '.',
        '']:
    print('%15s : %s' % (path, os.path.basename(path)))

print('######### os.path.dirname ###########')

for path in ['/one/two/three',
        '/one/two/three/',
        '/',
        '.',
        '']:
    print('%15s : %s' % (path, os.path.dirname(path)))

print('######### os.path.splitext ###########')

for path in ['filename',
        'filename.txt',
        '/path/to/filename.txt',
        '/',
        '',
        'my-archieve.tar.gz',
        'no-extention.']:
    print('%15s : %s' % (path, os.path.splitext(path)))

print('######### os.path.commonprefix ###########')

paths = ['/one/two/three',
        '/one/two/threefold',
        '/one/two/three/four']

for path in paths:
    print('PATH:', path)
print('PREFIX:', os.path.commonprefix(paths))

print('######### os.path.join ###########')

paths = [('one', 'two', 'three'),
        ('/', 'one', 'two', 'three'),
        ('/one', '/two', '/three', '/four'),
        ('one',)]

for path in paths:
    print('PATH:', os.path.join(*path))

print('######### os.path.expanduser ###########')
for user in ['', 'yang', 'yangge', 'shannon']:
    lookup = '~' + user
    print('%15s : %s' % (user, os.path.expanduser(lookup)))

print('######### os.path.expandvar ###########')
os.environ['MYVAR'] = 'VALUE'
print(os.path.expandvars('/home/yangge/$MYVAR'))
print(os.path.expandvars('/home/yangge/$PWD'))

print('######### os.path.normpath ###########')

paths = [('one//', 'two//', 'three'),
        ('/', 'one', '.', 'two', '.', 'three'),
        ('one', '..', 'alt', 'two', 'three', 'four'),
        ('one',)]

for path in paths:
    print('PATH:', os.path.join(*path))
    print('Normalized PATH:', os.path.normpath(os.path.join(*path)))

print('######### os.path.abspath ###########')

paths = ['.',
        '..',
        './one/two/three',
        '../one/two/threefold',
        'one/two/three/four']

for path in paths:
    print('PATH:', os.path.abspath(path))

print('######### os.path.time ###########')
print('%20s : ' % ('FILE'), __file__)
print('%20s : ' % ('ACESS TIME'), time.ctime(os.path.getatime(__file__)))
print('%20s : ' % ('MODIFIED TIME'), time.ctime(os.path.getmtime(__file__)))
print('%20s : ' % ('CHANGE TIME'), time.ctime(os.path.getctime(__file__)))

print('######### os.path.testfile ###########')
FILENAME = [__file__,
        os.path.dirname(__file__),
        '/',
        './broken_link'
        ]

for fn in FILENAME:
    print('%20s : ' % ('FILE'), fn)
    print('%20s : ' % ('Absobule'), os.path.isabs(fn))
    print('%20s : ' % ('Is file'), os.path.isfile(fn))
    print('%20s : ' % ('Is dir'), os.path.isdir(fn))
    print('%20s : ' % ('Is link'), os.path.islink(fn))
    print('%20s : ' % ('Mount point'), os.path.ismount(fn))
    print('%20s : ' % ('Exists'), os.path.exists(fn))
    print('%20s : ' % ('link Exists'), os.path.lexists(fn))
    print()

print('######### os.walk ###########')
if not os.path.exists('example'):
    os.mkdir('example')
if not os.path.exists('example/one'):
    os.mkdir('example/one')

with open('example/file.txt', 'wt') as f:
    f.write('contents')

with open('example/one/two.txt', 'wt') as f:
    f.write('contents')

for dirpath, dirnames, filenames in os.walk('example'):
    print(dirpath)
    for name in filenames:
        subname = os.path.join(dirpath, name)
        print(subname)
    for name in dirnames:
        subname = os.path.join(dirpath, name)
        print(subnamesubname+'/')
