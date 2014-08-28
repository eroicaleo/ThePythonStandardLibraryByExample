#!/usr/bin/env python3

import re

def show_banner(test_type):
    print('##'+'-'*100)
    print('##',test_type)
    print('##'+'-'*100)

bold = re.compile(r'\*{2}(.*?)\*{2}')

text = 'Make this **bold**. This **too**.'

print('Text: ', text)
print('Bold: ', bold.sub(r'<b>\1</b>', text))

show_banner('group with name')

bold = re.compile(r'\*{2}(?P<bold_text>.*?)\*{2}')

text = 'Make this **bold**. This **too**.'

print('Text: ', text)
print('Bold: ', bold.sub(r'<b>\g<bold_text></b>', text))

show_banner('replace with count')

print('Text: ', text)
print('Bold: ', bold.sub(r'<b>\g<bold_text></b>', text, count=1))

show_banner('subn')

print('Text: ', text)
print('Bold: ', bold.subn(r'<b>\g<bold_text></b>', text))
