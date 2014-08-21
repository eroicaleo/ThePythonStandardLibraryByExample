#!/usr/bin/env python3

import re

text = 'abbaaabbbaaaaa'
pattern = 'ab'

for match in re.findall(pattern, text):
    print('Found "%s"' % match)

for match in re.finditer(pattern, text):
    s = match.start()
    e = match.end()
    print('Found %s at %d to %d' % (text[s:e], s, e))
