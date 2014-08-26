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

test_patterns('abbaaabbbbaaaaa',
        [('a(ab)', "'a' followed by literal ab"),
         ('a(a*b*)', 'a followed by 0-n a and 0-n b'),
         ('a(ab)*', 'a followed by 0-n ab'),
         ('a(ab)+', 'a followed by 1-n ab'),
         ])


text = 'This is some text -- with punctuation.'

show_banner('groups')
print(text)

patterns = [
            (r'^(\w+)', "word at the start of string"),
            (r'(\w+)\S*\Z', "word at the end of string, with optional punctuation"),
            (r'(\bt\w+)\W+(\w+)', "word starts with t, another word"),
            (r'(\w+t)\b', "word ending with t"),
         ]

for pattern, desc in patterns:
    regexp = re.compile(pattern)
    match = regexp.search(text)
    print('Pattern %r (%s)\n' % (pattern, desc))
    print(match.groups())


show_banner('group')
print("%-30s:" % 'text', text)

regexp = re.compile(r'(\bt\w+)\W+(\w+)')
print("%-30s:" % 'pattern', regexp.pattern)
match = regexp.search(text)
print("%-30s:" % 'Entire match', match.group(0))
print("%-30s:" % 'word starting with "t"', match.group(1))
print("%-30s:" % 'word after the t word', match.group(2))

show_banner('group with name')
patterns = [
            (r'^(?P<first_word>\w+)', "word at the start of string"),
            (r'(?P<last_word>\w+)\S*\Z', "word at the end of string, with optional punctuation"),
            (r'(?P<t_word>\bt\w+)\W+(?P<other_word>\w+)', "word starts with t, another word"),
            (r'(?P<ends_with_t>\w+t)\b', "word ending with t"),
         ]

for pattern, desc in patterns:
    regexp = re.compile(pattern)
    match = regexp.search(text)
    print('Pattern %r (%s)\n' % (pattern, desc))
    print(match.groups())
    print(match.groupdict())

show_banner('nested groups')
def test_patterns(text, patterns=[]):
    for pattern, desc in patterns:
        print('Pattern %r (%s) \n' % (pattern, desc))
        print('%r' % text)
        for match in re.finditer(pattern, text):
            s = match.start()
            e = match.end()
            prefix = ' '*s
            print('%s%r%s'%(prefix, text[s:e], ' '*(len(text)-e)), end='   ')
            print(match.groups())
            if match.groupdict():
                print('%s%s' % (' '*(len(text) - e), match.groupdict()))
        print
    return

test_patterns(
        'abbaabba',
        [(r'a((a*)(b*))', 'a followed by 0-n a and 0-n b'),
            ]
        )

show_banner('nested groups')
test_patterns(
        'abbaaabba',
        [
            (r'a((a+)|(b+))', 'a followed by seq. of a or seq. of b'),
            (r'a((a|b)+)', 'a followed by seq. of [ab]'),
        ]
        )

show_banner('non capture')
test_patterns(
        'abbaaabba',
        [
            (r'a((a+)|(b+))', 'capture'),
            (r'a((?:a+)|(?:b+))', 'non capture'),
        ]
        )
