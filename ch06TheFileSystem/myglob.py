#!/usr/bin/env python3

import glob

for name in glob.glob('dir/*'):
    print(name)

print("#####################")
for name in glob.glob('dir/*/*'):
    print(name)

print("#####################")
for name in glob.glob('dir/subdir/*'):
    print(name)


print("#### question mark #######")
for name in glob.glob('dir/file?.txt'):
    print(name)

print("#### char range #######")
for name in glob.glob('dir/file[0-9].txt'):
    print(name)

print("#### iglob #######")
for name in glob.iglob('dir/*'):
    print(name)


