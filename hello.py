#!/usr/bin/python

# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 10:58:26 2017

@author: Sooraj Antony
"""


import sys
from dbUtils import dbTokenStatusChecker

ip = sys.argv[1]
token = sys.argv[2]
#write to file
f = open('tempBuffer.file', 'a')
f.write('\n The ip is ')  
f.write(ip)  
f.write('\n The token is ')  
f.write(token)
f.close()

#DbPrint
dbTokenStatusChecker(token , ip)



