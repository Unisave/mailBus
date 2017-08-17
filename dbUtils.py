#!/usr/bin/python

# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 10:58:26 2017

@author: Sooraj Antony
"""

import MySQLdb
def dbTokenStatusChecker(tokenNumber,tokenIP):
    try:
        db = MySQLdb.connect(host="192.168.1.14", user="mailBot", passwd="umn1234", db="mailBus") #AUTHENTICATION TO BE ENCRYPTED AND MOVED OUT SOON 
        #enable MySQL tunnel proxy for security ssh user@host.com -L 9990:localhost:3306
        cursor = db.cursor()
        cursor.execute ("""
                 SELECT token 
                 FROM mailBus.temptokenMapper
                 WHERE token = %s
               """, 
               (tokenNumber)
        )
        results = cursor.fetchall()
        # Check if anything at all is returned
        if results:
            print "Correct token"
            #SCRIPT TO LOG location and other details
            

        else:
            print "NO RESULTS RETURNED"
            #SCRIPT TO FLAG AND MARK BAD TOKEN GENERATED IP LOCATION using flaggedIP value
            print "BAD IP DETECTED:: " + tokenIP

    except MySQLdb.Error:
        print "ERROR IN CONNECTION"
    print "Execution completed"



