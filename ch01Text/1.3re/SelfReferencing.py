#!/usr/bin/env python3

import re

def show_banner(test_type):
    print('##'+'-'*100)
    print('##',test_type)
    print('##'+'-'*100)

address = re.compile(
    r'''
    # The regular name
    (\w+) # The first name
    \s+
    (([\w.]+)\s)? # optional middle name or initial
    (\w+) # The last name

    \s+

    <
    (?P<email>
        \1 # first name
        \.
        \4 # last name
        @
        ([\w\d.]+\.)+ # domain name prefix
        (com|org|edu) # limit the allowed top-level domains
    )
    >
    ''', re.VERBOSE | re.IGNORECASE)

candidates = [
        'first Last <first.last@example.com>',
        'Different Name <first.last@example.com>',
        'First Middle Last <first.last@example.com>',
        'First M. Last <first.last@example.com>',
        ]

for candidate in candidates:
    print('Candidate:', candidate)
    match = address.search(candidate)
    if match:
        print('NAME :', match.group(1), match.group(4))
        print('EMAIL:', match.group(5))
    else:
        print('No match')

show_banner('with names')

address = re.compile(
    r'''
    # The regular name
    (?P<first_name>\w+) # The first name
    \s+
    (([\w.]+)\s)? # optional middle name or initial
    (?P<last_name>\w+) # The last name

    \s+

    <
    (?P<email>
        (?P=first_name) # first name
        \.
        (?P=last_name) # last name
        @
        ([\w\d.]+\.)+ # domain name prefix
        (com|org|edu) # limit the allowed top-level domains
    )
    >
    ''', re.VERBOSE | re.IGNORECASE)

for candidate in candidates:
    print('Candidate:', candidate)
    match = address.search(candidate)
    if match:
        print('NAME :', match.group(1), match.group(4))
        print('EMAIL:', match.group(5))
        print(match.groups())
    else:
        print('No match')

show_banner('yes/no expression')
address = re.compile(
    '''
    ^
    # The regular name
    (?P<name>
     ([\w.]+\s+)*[\w.]+
    )?
    \s*

    # Email addresses are wrapped in angle brackets, but
    # only if a name is found.
    (?(name)
        (?P<brackets>(?=(<.*>$)))
        |
        (?=([^<].*[^>]$))
    )

    # Only look for a bracket if the look-ahead assertion
    # found both of them.
    (?(brackets)<|\s*)

    (?P<email>
    [\w\d.+-]+      # username
    @
    ([\w\d.]+\.)+   # domain name prefix
    (com|org|edu)   # domain
    )

    # Only look for a bracket if the look-ahead assertion
    # found both of them.
    (?(brackets)>|\s*)
    $
    ''', re.VERBOSE | re.IGNORECASE)

candidates = [
        'First Last <first.last@example.com>',
        'No Brackets first.last@example.com',
        'Open Bracket <first.last@example.com',
        'Close Bracket first.last@example.com>',
        'no.brackets@example.com',
        ]

for candidate in candidates:
    print('Candidate:', candidate)
    match = address.search(candidate)
    if match:
        print('NAME :', match.groupdict()['name'])
        print('EMAIL:', match.groupdict()['email'])
        print(match.groups())
    else:
        print('No match')

