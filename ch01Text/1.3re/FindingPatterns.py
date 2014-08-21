#!/usr/bin/env python3

import re

pattern = 'this'

text = 'Does this text match the pattern?'

match = re.search(pattern, text)

start = match.start()
end = match.end()

print('Found "%s"\nin "%s"\nfrom %d to %d ("%s")' % (match.re.pattern, match.string, start, end, text[start:end]))
