#!/usr/bin/env python3

import re

def show_banner(test_type):
    print('##'+'-'*100)
    print('##',test_type)
    print('##'+'-'*100)

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

show_banner('Non Greedy')
test_patterns('abbaaabbbbaaaaa',
        [('ab*?', "'a' followed by zero or more 'b'"),
         ('ab+?', "'a' followed by one or more 'b'"),
         ('ab??', "'a' followed by zero or one 'b'"),
         ('ab{3}?', "'a' followed by three 'b'"),
         ('ab{2,3}?', "'a' followed by two to three 'b'"),
         ])

show_banner('Character Set')
test_patterns('abbaaabbbbaaaaa',
        [('[ab]', "either 'a' or 'b'"),
         ('a[ab]+', "'a' followed by one or more 'a' or 'b'"),
         ('a[ab]+?', "'a' followed by one or more 'a' or 'b', not greedy"),
         ])

test_patterns('This is some text -- with punctuation.',
        [('[^-. ]+', "sequence without -, . or space"),
         ])

test_patterns('abbaabbba',
        [
            ('a.', "a followed by any one character"),
            ('b.', "b followed by any one character"),
            ('a.*b', "a followed by anything, ending in b"),
            ('a.*?b', "a followed by anything, ending in b"),
         ])

show_banner('Escape Codes')
