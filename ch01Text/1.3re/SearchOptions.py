#!/usr/bin/env python3

import re

def show_banner(test_type):
    print('##'+'-'*100)
    print('##',test_type)
    print('##'+'-'*100)

text = 'This is some text -- with punctuation.'
pattern = r'\bT\w+'
with_case = re.compile(pattern)
without_case = re.compile(pattern, re.IGNORECASE)

show_banner('IGNORECASE')
print('Text:\n  %s' % text)
print('Pattern:\n  %r' % pattern)
print('Case sensitive:')
for match in with_case.findall(text):
    print('  %r' % match)
print('Case insensitive:')
for match in without_case.findall(text):
    print('  %r' % match)

show_banner('MULTILINE')
text = 'This is some text -- with punctuation.\nA second line.'
pattern = r'(^\w+)|(\w+\S*$)'
single_line = re.compile(pattern)
multiline = re.compile(pattern, re.MULTILINE)

print('Text:\n  %s' % text)
print('Pattern:\n  %r' % pattern)
print('single line:')
for match in single_line.findall(text):
    print(' ', match)
    # We have to do it like this, `cause match is a tuple
    # print('  %r' % (match,))
print('multiple line:')
for match in multiline.findall(text):
    print('  %r' % (match,))

show_banner('DOTALL')
text = 'This is some text -- with punctuation.\nA second line.'
pattern = r'.+'
no_newlines = re.compile(pattern)
dotall = re.compile(pattern, re.DOTALL)

print('Text:\n  %s' % text)
print('Pattern:\n  %r' % pattern)
print('no newlines:')
for match in no_newlines.findall(text):
    print('  %r' % match)
print('dotall:')
for match in dotall.findall(text):
    print('  %r' % match)

show_banner('VERBOSE')

address = re.compile(r'[\w\d.+-]+@([\w\d.]+\.)+(com|org|edu)')

candidates = [
        'first.last@example.com',
        'first.last+category@gmail.com',
        'valid-address@mail.example.com',
        'not-valid@example.foo',
        ]

for candidate in candidates:
    match = address.match(candidate)
    print('%-30s'%candidate, 'Match' if match else 'Not match')

address = re.compile(
    '''
    [\w\d.+-]+      # username
    @
    ([\w\d.]+\.)+   # domain name prefix
    (com|org|edu)   # domain
    ''',
    re.VERBOSE)

for candidate in candidates:
    match = address.match(candidate)
    print('%-30s'%candidate, 'Match' if match else 'Not match')

address = re.compile(
    '''
    (
    (?P<name>
    ([\w.,]+\s+)*([\w.,]+)
    )
    \s*
    <
    )?

    # The address it self
    (?P<email>
    [\w\d.+-]+      # username
    @
    ([\w\d.]+\.)+   # domain name prefix
    (com|org|edu)   # domain
    )

    >?
    ''',
    re.VERBOSE)

candidates = [
        'first.last@example.com',
        'first.last+category@gmail.com',
        'valid-address@mail.example.com',
        'not-valid@example.foo',
        'First Last <first.last@example.com>',
        'No Brackets first.last@example.com',
        'First Last',
        'First Middle Last <first.last@example.com>',
        'First M. Last <first.last@example.com>',
        '<first.last@example.com>',
        ]

for candidate in candidates:
    print('Candidate:', candidate)
    match = address.search(candidate)
    if match:
        print('NAME :', match.groupdict()['name'])
        print('EMAIL:', match.groupdict()['email'])
    else:
        print('No match')

show_banner('embedded flag')

text = 'This is some text -- with punctuation.'
pattern = r'\bT\w+'
with_case = re.compile(pattern)
pattern = r'(?i)\bT\w+'
without_case = re.compile(pattern)

print('Text:\n  %s' % text)
print('Pattern:\n  %r' % pattern)
print('Case sensitive:')
for match in with_case.findall(text):
    print('  %r' % match)
print('Case insensitive:')
for match in without_case.findall(text):
    print('  %r' % match)
