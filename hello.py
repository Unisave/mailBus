#!/usr/bin/python

# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 10:58:26 2017

@author: Sooraj Antony
"""


import sys

ip = sys.argv[1]
#write to file
f = open('tempBuffer.file', 'a')
f.write('\n The ip is')  
f.write(ip)  
f.close()
