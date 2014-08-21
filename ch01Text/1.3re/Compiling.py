#!/usr/bin/env python3

import re

regexps = [re.compile(p) for p in ['this', 'that']]

text = 'Does this text match the pattern?'

print('Text: %r\n', text)

for regexp in regexps:
    print('Seeking "%s" ->' % regexp.pattern, end=' ')

    if regexp.search(text):
        print('Match!')
    else:
        print('No Match!')
