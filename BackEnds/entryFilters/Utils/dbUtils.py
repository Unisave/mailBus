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
from valueUpdateAppender import valueUpdateAppender

#variableDeclarations
mysqlHostIP="192.168.1.14"
mysqlUser="mailBot"
mysqlHackuser="hackLog"
mysqlPasswd="umn1234"
mysqlDBName="mailBus"
connectionErrorMsgMysql = " "
executionCompleteMsg = " "
emptyResultsMsg = " "


def valueUpdateAppender(varA, varB):
    try:
        dbA = MySQLdb.connect(host=mysqlHostIP, user=mysqlUser, passwd=mysqlPasswd, db=mysqlDBName) #AUTHENTICATION TO BE ENCRYPTED AND MOVED OUT SOON 

        #enable MySQL tunnel proxy for security ssh user@host.com -L 9990:localhost:3306
        cursorA = dbA.cursor()
        
        cursorA.execute (""" 
            SELECT %s 
            FROM tokenStatusHandler 
            WHERE token = '%s'
            """ 
            % (varA , varB)
            )
        # outValue = cursorA.fetchone()
        outValues = cursorA.fetchone()
        # while outValues is not None:
        outValue =  outValues[0]
            # cursorA.fetchone()


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
        # print var4
        db1 = MySQLdb.connect(host=mysqlHostIP, user=mysqlUser, passwd=mysqlPasswd, db=mysqlDBName) #AUTHENTICATION TO BE ENCRYPTED AND MOVED OUT SOON 
        #enable MySQL tunnel proxy for security ssh user@host.com -L 9990:localhost:3306
        cursor1 = db1.cursor()
        cursor1.execute (""" INSERT INTO bad_Tokens_temp(token, TIMESTAMPER, badIP, geoTracker) 
            VALUES ('%s', '%s', '%s', '%s') """
             % (var1, var2, var3, var4))
        results1 = cursor1.fetchall()
        db1.commit()
        db1.close()
        # print results1
        responseNoToken = "BAD TOKEN ENTRY DETECTED FOR TOKEN NUMBER:: " + tokenNumber + " TRIGGERED AT " + triggerTime + " FROM " + tokenIP 
        # print  responseNoToken
    except MySQLdb.Error:
        print connectionErrorMsgMysql 
        print MySQLdb.Error
    print executionCompleteMsg



def hackAttemptExist(tokenIP,triggerTime):
    try:
        var1 = tokenIP
        var2 = triggerTime
        dbX = MySQLdb.connect(host=mysqlHostIP, user=mysqlHackuser, passwd=mysqlPasswd, db=mysqlDBName) #AUTHENTICATION TO BE ENCRYPTED AND MOVED OUT SOON 
        #enable MySQL tunnel proxy for security ssh user@host.com -L 9990:localhost:3306
        cursorX = dbX.cursor()
        cursorX.execute (""" INSERT INTO hackLog(IPLOG, TIMELOG)
            VALUES ('%s', '%s') """ 
            % (var1, var2))
        resultsX = cursorX.fetchall()
        dbX.commit()
        dbX.close()
        # print results1
        # responseNoToken = "HACK TOKEN ENTRY RECORDED FROM:: " + tokenIP + " TRIGGERED AT " + triggerTime
        # print  responseNoToken
    except MySQLdb.Error:
        print connectionErrorMsgMysql 
        print MySQLdb.Error
    print executionCompleteMsg
 


from valueUpdateAppender import valueUpdateAppender


def tokenExist(tokenNumber,tokenIP,triggerTime,geoJS):
    try:
        var1 = tokenNumber
        var2 = triggerTime
        var3 = tokenIP
        var4 = " ("+unicode(geoJS['longitude']) +" :: "+ unicode(geoJS['latitude']) +") , "+ unicode(geoJS['city']) +" , "+ unicode(geoJS['region_name']) +" , "+ unicode(geoJS['zip_code']) +" , "+ unicode(geoJS['country_name'])
    #var5 = numberOfOpens #UNUSED PLACEHOLDER
        db2 = MySQLdb.connect(host=mysqlHostIP, user=mysqlUser, passwd=mysqlPasswd, db=mysqlDBName) #AUTHENTICATION TO BE ENCRYPTED AND MOVED OUT SOON 
        #enable MySQL tunnel proxy for security ssh user@host.com -L 9990:localhost:3306
        cursor2 = db2.cursor()
        cursor2.execute ("""
                 SELECT token 
                 FROM tokenStatusHandler
                 WHERE token = '%s'
               """, 
               (tokenNumber)
        )
        results2 = cursor2.fetchall()
        if results2:
            # print "Correct token (" + tokenNumber + ") TRIGGERED AT " + triggerTime + " FROM " + tokenIP 
            #SCRIPT TO LOG location and other details
            TIMESTAMPER = valueUpdateAppender('TIMESTAMPER' , var1)
            numberOfOpens = valueUpdateAppender('numberOfOpens' , var1)
            openedLocationIP = valueUpdateAppender('openedLocationIP' , var1)
            openGeoLocation = valueUpdateAppender('openGeoLocation' , var1)

            # print "OLD ENTRY RAW"
            # print TIMESTAMPER
            # print numberOfOpens
            # print openedLocationIP
            # print openGeoLocation

            # print "NEW ENTRY RAW"
            # print var2
            # print var3
            # print var4

            var2 = "{" + unicode(var2) + " } , "
            var3 = "{" + unicode(var3) + " } , "
            var4 = "{" + unicode(var4) + " } , "

            # print "NEW ENTRY PRETTY"
            # print var2
            # print var3
            # print var4


            var2 += unicode(TIMESTAMPER)
            var5 = int(numberOfOpens) + 1
            var3 += unicode(openedLocationIP)
            var4 += unicode(openGeoLocation)

            # print "FINAL format"
            # print var2
            # print var3
            # print var4
            # print var5
            # print var1
            try:
                cursor3 = db2.cursor()
                cursor3.execute (""" 
                    UPDATE `tokenStatusHandler`
                    SET TIMESTAMPER='%s', numberOfOpens='%s', openedLocationIP='%s', openGeoLocation='%s' 
                    WHERE token = '%s'
                    """ 
                    % (unicode(var2), unicode(var5), unicode(var3), unicode(var4), unicode(var1)))
                results3 = cursor3.fetchall()
                # print results3
            except MySQLdb.Error:
                print connectionErrorMsgMysql 
                print MySQLdb.Error
            print executionCompleteMsg
        else:
            try:
                var2 = "{" + unicode(var2) + " }"
                var3 = "{" + unicode(var3) + " }"
                var4 = "{" + unicode(var4) + " }"
                cursor4 = db2.cursor()
                cursor4.execute (""" 
                    INSERT INTO tokenStatusHandler (numberOfOpens, token, openedLocationIP, TIMESTAMPER, openGeoLocation) 
                    VALUES ('1', '%s', '%s', '%s', '%s')
                    """ 
                    % (unicode(var1), unicode(var3), unicode(var2), unicode(var4)))
                results4 = cursor4.fetchall()
                # print results4
            except MySQLdb.Error:
                print connectionErrorMsgMysql 
                print MySQLdb.Error
            print executionCompleteMsg


            # cursor3.execute (" INSERT INTO mailBus.tokenStatusHandler (TIMESTAMPER, token, numberOfOpens, openedLocationIP, openGeoLocation) VALUES ('%s', '%s', '%s', '%s', '%s');" % (var2, var1, , var3, ))
        db2.commit()
        db2.close()
        # print resultsa
        # responseNoToken = "BAD TOKEN ENTRY DETECTED FOR TOKEN NUMBER:: " + tokenNumber + " TRIGGERED AT " + triggerTime + " FROM " + tokenIP 
        # print  responseNoToken
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
                 WHERE token = '%s'
               """, 
               (tokenNumber)
        )
        results = cursor.fetchall()
        db.close()
        # Check if anything at all is returned
        if results:
            # print "Correct token (" + tokenNumber + ") TRIGGERED AT " + triggerTime + " FROM " + tokenIP 
            #SCRIPT TO LOG location and other details
            tokenExist(tokenNumber,tokenIP,triggerTime,geoJS)
        else:
            # print emptyResultsMsg
            noTokenExist(tokenNumber,tokenIP,triggerTime,geoJS)
    except MySQLdb.Error:
        print connectionErrorMsgMysql 
        print MySQLdb.Error
    print executionCompleteMsg
