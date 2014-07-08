#!/usr/bin/env python3

import os.path

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

print('######### os.path.splitext ###########')

paths = ['/one/two/three',
        '/one/two/threefold',
        '/one/two/three/four']

for path in paths:
    print('PATH:', path)
print('PREFIX:', os.path.commonprefix(paths))


