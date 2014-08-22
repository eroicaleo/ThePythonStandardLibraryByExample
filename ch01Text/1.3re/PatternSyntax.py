#!/usr/bin/env python3

import re

def test_patterns(text, patterns=[]):
    for pattern, desc in patterns:
        print('Pattern %r (%s) \n' % (pattern, desc))
        print('%r' % text)
        for match in re.finditer(pattern, text):
            s = match.start()
            e = match.end()
            substr = text[s:e]
            n_backslashes = text[:s].count('\\')
            prefix = '.' * (s + n_backslashes)
            print('%s%r' % (prefix, substr))

test_patterns('abbaaabbbbaaaaa', [('ab', "'a' followed by 'b'")])


test_patterns('abbaaabbbbaaaaa',
        [('ab*', "'a' followed by zero or more 'b'"),
         ('ab+', "'a' followed by one or more 'b'"),
         ('ab?', "'a' followed by zero or one 'b'"),
         ('ab{3}', "'a' followed by three 'b'"),
         ('ab{2,3}', "'a' followed by two to three 'b'"),
         ])

print('##'+'-'*100)
print('##','Non greedy')
print('##'+'-'*100)
test_patterns('abbaaabbbbaaaaa',
        [('ab*?', "'a' followed by zero or more 'b'"),
         ('ab+?', "'a' followed by one or more 'b'"),
         ('ab??', "'a' followed by zero or one 'b'"),
         ('ab{3}?', "'a' followed by three 'b'"),
         ('ab{2,3}?', "'a' followed by two to three 'b'"),
         ])

print('##'+'-'*100)
print('##','Character Set')
print('##'+'-'*100)
test_patterns('abbaaabbbbaaaaa',
        [('[ab]', "either 'a' or 'b'"),
         ('a[ab]+', "'a' followed by one or more 'a' or 'b'"),
         ('a[ab]+?', "'a' followed by one or more 'a' or 'b', not greedy"),
         ])
