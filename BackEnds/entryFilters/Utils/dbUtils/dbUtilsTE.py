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
from dbUtilsVUA import valueUpdateAppender


#variableDeclarations
with open('./BackEnds/entryFilters/Utils/dbUtils/trackerDBConfig.json') as json_auth_file:
    authdata = json.load(json_auth_file)
    db2mysqlHostIP = authdata["TonStatHlrSel"]["HostIP"]
    db2mysqlUser = authdata["TonStatHlrSel"]["User"]
    db2mysqlPasswd = authdata["TonStatHlrSel"]["Passwd"]
    db2mysqlDBName = authdata["TonStatHlrSel"]["DBName"]
    db3mysqlHostIP = authdata["TonStatHlrUpd"]["HostIP"]
    db3mysqlUser = authdata["TonStatHlrUpd"]["User"]
    db3mysqlPasswd = authdata["TonStatHlrUpd"]["Passwd"]
    db3mysqlDBName = authdata["TonStatHlrUpd"]["DBName"]
    db4mysqlHostIP = authdata["TonStatHlrIns"]["HostIP"]
    db4mysqlUser = authdata["TonStatHlrIns"]["User"]
    db4mysqlPasswd = authdata["TonStatHlrIns"]["Passwd"]
    db4mysqlDBName = authdata["TonStatHlrIns"]["DBName"]

with open('./BackEnds/entryFilters/Utils/dbUtils/dbResponses.json') as json_response_file:
    respodata = json.load(json_response_file)
    connectionErrorMsgMysql = respodata["TEResponses"]["connectionErrorMsgMysql"]
    executionCompleteMsg = respodata["TEResponses"]["executionCompleteMsg"]


def tokenExist(tokenNumber,tokenIP,triggerTime,geoJS):
    try:
        var1 = tokenNumber
        var2 = triggerTime
        var3 = tokenIP
        var4 = " ("+unicode(geoJS['longitude']) +" :: "+ unicode(geoJS['latitude']) +") , "+ unicode(geoJS['city']) +" , "+ unicode(geoJS['region_name']) +" , "+ unicode(geoJS['zip_code']) +" , "+ unicode(geoJS['country_name'])
        db2 = MySQLdb.connect(host=db2mysqlHostIP, user=db2mysqlUser, passwd=db2mysqlPasswd, db=db2mysqlDBName)
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
        db2.commit()
        db2.close()
        if results2:
            numberOfOpens = valueUpdateAppender('numberOfOpens' , var1)
            TIMESTAMPER = valueUpdateAppender('TIMESTAMPER' , var1)
            openedLocationIP = valueUpdateAppender('openedLocationIP' , var1)
            openGeoLocation = valueUpdateAppender('openGeoLocation' , var1)
            var2 = "{" + unicode(var2) + " } , " + unicode(TIMESTAMPER)
            var3 = "{" + unicode(var3) + " } , " + unicode(openedLocationIP)
            var4 = "{" + unicode(var4) + " } , " + unicode(openGeoLocation)
            var5 = int(numberOfOpens) + 1
            
            
            
            try:
                db3 = MySQLdb.connect(host=db3mysqlHostIP, user=db3mysqlUser, passwd=db3mysqlPasswd, db=db3mysqlDBName)
                cursor3 = db3.cursor()
                cursor3.execute (""" 
                    UPDATE `tokenStatusHandler`
                    SET TIMESTAMPER='%s', numberOfOpens='%s', openedLocationIP='%s', openGeoLocation='%s' 
                    WHERE token = '%s'
                    """ 
                    % (unicode(var2), unicode(var5), unicode(var3), unicode(var4), unicode(var1)))
                results3 = cursor3.fetchall()
                db3.commit()
                db3.close()
            except MySQLdb.Error:
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
                    INSERT INTO tokenStatusHandler (numberOfOpens, token, openedLocationIP, TIMESTAMPER, openGeoLocation) 
                    VALUES ('1', '%s', '%s', '%s', '%s')
                    """ 
                    % (unicode(var1), unicode(var3), unicode(var2), unicode(var4)))
                results4 = cursor4.fetchall()
                db4.commit()
                db4.close()
            except MySQLdb.Error:
                print connectionErrorMsgMysql 
                print MySQLdb.Error
            print executionCompleteMsg

    except MySQLdb.Error:
        print connectionErrorMsgMysql 
        print MySQLdb.Error
    print executionCompleteMsg
 
