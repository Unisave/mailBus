#!/usr/bin/python

# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 10:58:26 2017

@author: Sooraj Antony
"""

import cgi
import MySQLdb

try:
    db = MySQLdb.connect(host="127.0.0.1", user="root", passwd="umn1234", db="admin_logger")
    cursor = db.cursor()        
    cursor.execute("SHOW TABLES;")
    results = cursor.fetchall()
    # Check if anything at all is returned
    if results:
        print results[0]
    else:
        print "getr"               
except MySQLdb.Error:
    print "ERROR IN CONNECTION"
print "getrqw"