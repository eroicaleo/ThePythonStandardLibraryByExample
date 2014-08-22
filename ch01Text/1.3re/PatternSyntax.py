#!/usr/bin/env python3

import re

def test_patterns(text, patterns=[]):
    for pattern, desc in patterns:
        print('Pattern %r (%s) \n' % (pattern, desc))
        print('  %r' % text)
