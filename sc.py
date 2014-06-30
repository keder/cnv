#! /usr/bin/env python
# -*- coding: utf-8 -*-


import traceback
from urllib import unquote_plus


input_string = "%D0%B0"
input_string = unquote_plus(input_string)
print input_string
f = open('/home/keder/test.txt', 'w')
f.write(input_string)
