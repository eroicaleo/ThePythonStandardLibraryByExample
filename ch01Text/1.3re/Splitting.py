#!/usr/bin/env python3

import re

text = '''Paragraph one
on two lines.

Paragraph two.


Paragraph three.'''

for num, para in enumerate(re.findall(r'(.+?)\n{2,}', text, re.DOTALL)):
    print(num, repr(para))
    print()

print('With find all:')

for num, para in enumerate(re.findall(r'(.+?)(\n{2,}|$)', text, re.DOTALL)):
    print(num, repr(para))
    print()

print('With split:')

for num, para in enumerate(re.split(r'\n{2,}', text, re.DOTALL)):
    print(num, repr(para))
    print()

print('With split again:')

for num, para in enumerate(re.split(r'(\n{2,})', text, re.DOTALL)):
    print(num, repr(para))
    print()

text = 'aabaaabaaaab'
for match in re.findall(r'(.+?)b', text):
    print(match)
