#!/usr/bin/python

# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 10:58:26 2017

@author: Sooraj Antony
"""
#System Libraries
import MySQLdb

#UserLibraries
from valHandler import location


#variableDeclarations
mysqlHostIP="192.168.1.14"
mysqlUser="mailBot"
mysqlPasswd="umn1234"
mysqlDBName="mailBus"
connectionErrorMsgMysql = "ERROR IN CONNECTION"
executionCompleteMsg = "Execution completed"
emptyResultsMsg = "NO RESULTS RETURNED"



def valueUpdateAppender(varA, varB):
    try:
        dbA = MySQLdb.connect(host=mysqlHostIP, user=mysqlUser, passwd=mysqlPasswd, db=mysqlDBName) #AUTHENTICATION TO BE ENCRYPTED AND MOVED OUT SOON 

        #enable MySQL tunnel proxy for security ssh user@host.com -L 9990:localhost:3306
        cursorA = dbA.cursor()
        
        cursorA.execute (""" 
            SELECT %s 
            FROM tokenStatusHandler 
            WHERE token = '%s'
            """, 
            (varA , varB)
            )
        outValue = cursorA.fetchall()
        print varA + " is " + outValue
        dbA.close
        return(outValue)
    except MySQLdb.Error:
        print connectionErrorMsgMysql 
        print MySQLdb.Error
    print executionCompleteMsg






def noTokenExist(tokenNumber,tokenIP,triggerTime,geoJS):
    try:
        var1 = tokenNumber
        var2 = triggerTime
        var3 = tokenIP
        var4 = " ("+unicode(geoJS['longitude']) +" :: "+ unicode(geoJS['latitude']) +") , "+ unicode(geoJS['city']) +" , "+ unicode(geoJS['region_name']) +" , "+ unicode(geoJS['zip_code']) +" , "+ unicode(geoJS['country_name'])
        print var4
        db1 = MySQLdb.connect(host=mysqlHostIP, user=mysqlUser, passwd=mysqlPasswd, db=mysqlDBName) #AUTHENTICATION TO BE ENCRYPTED AND MOVED OUT SOON 
        #enable MySQL tunnel proxy for security ssh user@host.com -L 9990:localhost:3306
        cursor1 = db1.cursor()
        cursor1.execute (""" INSERT INTO bad_Tokens_temp(token, TIMESTAMPER, badIP, geoTracker) 
            VALUES ('%s', '%s', '%s', '%s') """
             % (var1, var2, var3, var4))
        results1 = cursor1.fetchall()
        db1.commit()
        db1.close()
        print results1
        responseNoToken = "BAD TOKEN ENTRY DETECTED FOR TOKEN NUMBER:: " + tokenNumber + " TRIGGERED AT " + triggerTime + " FROM " + tokenIP 
        print  responseNoToken
    except MySQLdb.Error:
        print connectionErrorMsgMysql 
        print MySQLdb.Error
    print executionCompleteMsg
 




def tokenExist(tokenNumber,tokenIP,triggerTime,geoJS):
    try:
        var1 = tokenNumber
        var2 = triggerTime
        var3 = tokenIP
        var4 = " ("+unicode(geoJS['longitude']) +" :: "+ unicode(geoJS['latitude']) +") , "+ unicode(geoJS['city']) +" , "+ unicode(geoJS['region_name']) +" , "+ unicode(geoJS['zip_code']) +" , "+ unicode(geoJS['country_name'])
        db2 = MySQLdb.connect(host=mysqlHostIP, user=mysqlUser, passwd=mysqlPasswd, db=mysqlDBName) #AUTHENTICATION TO BE ENCRYPTED AND MOVED OUT SOON 
        #enable MySQL tunnel proxy for security ssh user@host.com -L 9990:localhost:3306
        cursor2 = db2.cursor()
        cursor2.execute ("""
                 SELECT token 
                 FROM tokenStatusHandler
                 WHERE token = %s
               """, 
               (tokenNumber)
        )
        results2 = cursor2.fetchall()
        cursor3 = db2.cursor()
        if results2:
            print "Correct token (" + tokenNumber + ") TRIGGERED AT " + triggerTime + " FROM " + tokenIP 
            #SCRIPT TO LOG location and other details
            TIMESTAMPER = valueUpdateAppender('TIMESTAMPER' , var1)
            numberOfOpens = valueUpdateAppender('numberOfOpens' , var1)
            openedLocationIP = valueUpdateAppender('openedLocationIP' , var1)
            openGeoLocation = valueUpdateAppender('openGeoLocation' , var1)
            print "Final added aggregated values::" + unicode(TIMESTAMPER)
            print "Final added aggregated values::" + unicode(numberOfOpens)
            print "Final added aggregated values::" + unicode(openedLocationIP)
            print "Final added aggregated values::" + unicode(openGeoLocation)
        else:
            print "NOT STARTED due to no copy"
            # cursor3.execute (" INSERT INTO mailBus.tokenStatusHandler (TIMESTAMPER, token, numberOfOpens, openedLocationIP, openGeoLocation) VALUES ('%s', '%s', '%s', '%s', '%s');" % (var2, var1, , var3, ))
        results3 = cursor3.fetchall()
        db2.commit()
        db2.close()
        print resultsa
        responseNoToken = "BAD TOKEN ENTRY DETECTED FOR TOKEN NUMBER:: " + tokenNumber + " TRIGGERED AT " + triggerTime + " FROM " + tokenIP 
        print  responseNoToken
    except MySQLdb.Error:
        print connectionErrorMsgMysql 
        print MySQLdb.Error
    print executionCompleteMsg
 






def dbTokenStatusChecker(tokenNumber,tokenIP,triggerTime):
    try:
        geoJS = location(tokenIP)
        # geoAddress = geoJS['longitude'] + "," + geoJS['latitude' + "," + geoJS['city'] + "," +  geoJS['region_name'] + "," +  geoJS['zip_code'] + "," +  geoJS['country_name']
        # print geoJS
        
        db = MySQLdb.connect(host=mysqlHostIP, user=mysqlUser, passwd=mysqlPasswd, db=mysqlDBName) #AUTHENTICATION TO BE ENCRYPTED AND MOVED OUT SOON 
        #enable MySQL tunnel proxy for security ssh user@host.com -L 9990:localhost:3306
        cursor = db.cursor()
        cursor.execute ("""
                 SELECT token 
                 FROM temptokenMapper
                 WHERE token = %s
               """, 
               (tokenNumber)
        )
        results = cursor.fetchall()
        db.close()
        # Check if anything at all is returned
        if results:
            print "Correct token (" + tokenNumber + ") TRIGGERED AT " + triggerTime + " FROM " + tokenIP 
            #SCRIPT TO LOG location and other details
            tokenExist(tokenNumber,tokenIP,triggerTime,geoJS)
        else:
            print emptyResultsMsg
            noTokenExist(tokenNumber,tokenIP,triggerTime,geoJS)
    except MySQLdb.Error:
        print connectionErrorMsgMysql 
        print MySQLdb.Error
    print executionCompleteMsg
