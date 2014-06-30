#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 16:22:27 2012

@author: keder
"""
import os
import sys
from wsgiref.simple_server import make_server
from cgi import parse_qs, escape

def application(environ, start_response):
	try:
		request_body_size = int(environ.get('CONTENT_LENGTH', 0))
	except (ValueError):
		request_body_size = 0
		
	request_body = environ['wsgi.input'].read(request_body_size)
	f = open("/home/n/newfate/test/public_html/wsgi/test.txt", "w")
	f.write(request_body)
	
mytext = open(os.environ["SCRIPT_FILENAME"]).read()
f = open("/home/n/newfate/test/public_html/wsgi/test.txt", "w")
f.write(mytext)