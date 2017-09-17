#!/usr/bin/python

# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 10:58:26 2017

@author: Sooraj Antony
"""


#System Libraries
import MySQLdb
import json

#UserLibraries
from dbUtilsCVUA import valueClickUpdateAppender


#variableDeclarations
with open('./BackEnds/entryFilters/Utils/dbUtils/trackerDBConfig.json') as json_auth_file:
    authdata = json.load(json_auth_file)
    db2mysqlHostIP = authdata["TrakStatHlrSel"]["HostIP"]
    db2mysqlUser = authdata["TrakStatHlrSel"]["User"]
    db2mysqlPasswd = authdata["TrakStatHlrSel"]["Passwd"]
    db2mysqlDBName = authdata["TrakStatHlrSel"]["DBName"]
    db3mysqlHostIP = authdata["TrakStatHlrUpd"]["HostIP"]
    db3mysqlUser = authdata["TrakStatHlrUpd"]["User"]
    db3mysqlPasswd = authdata["TrakStatHlrUpd"]["Passwd"]
    db3mysqlDBName = authdata["TrakStatHlrUpd"]["DBName"]
    db4mysqlHostIP = authdata["TrakStatHlrIns"]["HostIP"]
    db4mysqlUser = authdata["TrakStatHlrIns"]["User"]
    db4mysqlPasswd = authdata["TrakStatHlrIns"]["Passwd"]
    db4mysqlDBName = authdata["TrakStatHlrIns"]["DBName"]


with open('./BackEnds/entryFilters/Utils/dbUtils/dbResponses.json') as json_response_file:
    respodata = json.load(json_response_file)
    connectionErrorMsgMysql = respodata["CTEResponses"]["connectionErrorMsgMysql"]
    executionCompleteMsg = respodata["CTEResponses"]["executionCompleteMsg"]


def trackerExist(trackerNumber,trackerIP,triggerTime,geoJS):
    try:
        var1 = trackerNumber
        var2 = triggerTime
        var3 = trackerIP
        var4 = " ("+unicode(geoJS['longitude']) +" :: "+ unicode(geoJS['latitude']) +") , "+ unicode(geoJS['city']) +" , "+ unicode(geoJS['region_name']) +" , "+ unicode(geoJS['zip_code']) +" , "+ unicode(geoJS['country_name'])
        db2 = MySQLdb.connect(host=db2mysqlHostIP, user=db2mysqlUser, passwd=db2mysqlPasswd, db=db2mysqlDBName)
        #enable MySQL tunnel proxy for security ssh user@host.com -L 9990:localhost:3306
        cursor2 = db2.cursor()
        cursor2.execute ("""
                 SELECT tracker 
                 FROM trackerStatusHandler
                 WHERE tracker = %s
               """, 
               (trackerNumber)
        )
        results2 = cursor2.fetchall()
        db2.commit()
        db2.close()
        if results2:
            numberOfClicks = valueClickUpdateAppender('numberOfClicks' , var1)
            TIMESTAMPER = valueClickUpdateAppender('TIMESTAMPER' , var1)
            openedLocationIP = valueClickUpdateAppender('openedLocationIP' , var1)
            openGeoLocation = valueClickUpdateAppender('openGeoLocation' , var1)
            var2 = "{" + unicode(var2) + " } , " + unicode(TIMESTAMPER)
            var3 = "{" + unicode(var3) + " } , " + unicode(openedLocationIP)
            var4 = "{" + unicode(var4) + " } , " + unicode(openGeoLocation)
            var5 = int(numberOfClicks) + 1
            
            
            
            try:
                db3 = MySQLdb.connect(host=db3mysqlHostIP, user=db3mysqlUser, passwd=db3mysqlPasswd, db=db3mysqlDBName)
                cursor3 = db3.cursor()
                cursor3.execute (""" 
                    UPDATE `trackerStatusHandler`
                    SET TIMESTAMPER='%s', numberOfClicks='%s', openedLocationIP='%s', openGeoLocation='%s' 
                    WHERE tracker = '%s'
                    """ 
                    % (unicode(var2), unicode(var5), unicode(var3), unicode(var4), unicode(var1)))
                results3 = cursor3.fetchall()
                db3.commit()
                db3.close()
            except MySQLdb.Error:
                print "2nd" 
                print connectionErrorMsgMysql 
                print MySQLdb.Error
            print executionCompleteMsg
        else:
            try:
                var2 = "{" + unicode(var2) + " }"
                var3 = "{" + unicode(var3) + " }"
                var4 = "{" + unicode(var4) + " }"
                db4 = MySQLdb.connect(host=db4mysqlHostIP, user=db4mysqlUser, passwd=db4mysqlPasswd, db=db4mysqlDBName)
                cursor4 = db4.cursor()
                cursor4.execute (""" 
                    INSERT INTO trackerStatusHandler (numberOfClicks, tracker, openedLocationIP, TIMESTAMPER, openGeoLocation) 
                    VALUES ('1', '%s', '%s', '%s', '%s')
                    """ 
                    % (unicode(var1), unicode(var3), unicode(var2), unicode(var4)))
                results4 = cursor4.fetchall()
                db4.commit()
                db4.close()
            except MySQLdb.Error:
                print "3rd" 
                print connectionErrorMsgMysql 
                print MySQLdb.Error
            print executionCompleteMsg

    except MySQLdb.Error:
        print "1st" 
        print connectionErrorMsgMysql 
        print MySQLdb.Error
    print executionCompleteMsg
 
