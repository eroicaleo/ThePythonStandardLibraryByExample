#!/usr/bin/env python3

import re

def show_banner(test_type):
    print('##'+'-'*100)
    print('##',test_type)
    print('##'+'-'*100)

show_banner('look ahead')
address = re.compile(
    '''
    # A name is made up of letters, and may include "."
    # for title abbreviations and middle initials.
    ((?P<name>
        ([\w.,]+\s+)*([\w.,]+)
     )
     \s+
    ) # name is no longer optional

    # LOOKAHEAD
    # Email addresses are wrapped in angle brackets, but only
    # if they are both present or neither is.
    (?=(<.*>$)       # reminder wrapped in angle brackets
       |
       ([^<].*[^>]$) # reminder *not* wrapped in angle brackets
    )

    <? # optional opening angle bracket
    # The address it self
    (?P<email>
    [\w\d.+-]+      # username
    @
    ([\w\d.]+\.)+   # domain name prefix
    (com|org|edu)   # domain
    )

    >? # optional opening angle bracket
    ''',
    re.VERBOSE)

candidates = [
        'First Last <first.last@example.com>',
        'No Brackets first.last@example.com',
        'Open Bracket <first.last@example.com',
        'Close Bracket first.last@example.com>',
        ]

for candidate in candidates:
    print('Candidate:', candidate)
    match = address.search(candidate)
    if match:
        print('NAME :', match.groupdict()['name'])
        print('EMAIL:', match.groupdict()['email'])
        print(match.groups())
        print(match.groupdict())
    else:
        print('No match')

show_banner('negative look ahead')
address = re.compile(
        '''
        (?x)
        ^
        # An address: username@domain.tld

        # Ignore noreply addresses
        (?!noreply@.*$)

        [\w\d.+-]+      # username
        @
        ([\w\d.]+\.)+   # domain name prefix
        (com|org|edu)   # domain

        $
        ''')

candidates = [
        'first.last@example.com',
        'noreply@example.com',
        ]

for candidate in candidates:
    print('Candidate:', candidate)
    match = address.search(candidate)
    if match:
        print('EMAIL:', candidate[match.start():match.end()])
    else:
        print('No match')

show_banner('negative look backward')
