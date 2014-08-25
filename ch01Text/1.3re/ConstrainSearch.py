#!/usr/bin/env python3

import re

text = 'This is some text -- with punctuation.'
pattern = 'is'

print('Text   :', text)
print('Pattern:', pattern)

m = re.match(pattern, text)
print('Match  :', m)
s = re.search(pattern, text)
print('Search :', s)

pattern = re.compile(r'\b\w*is\w*\b')
print('Text:', text)

pos = 0
while True:
    match = pattern.search(text, pos)
    if not match:
        break
    s = match.start()
    e = match.end()
    print(' %2d : %2d = "%s"' % (s, e-1, text[s:e]))
    pos = e
