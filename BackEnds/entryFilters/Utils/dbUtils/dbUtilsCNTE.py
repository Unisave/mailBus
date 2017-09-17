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


#variableDeclarations
with open('./BackEnds/entryFilters/Utils/dbUtils/trackerDBConfig.json') as json_auth_file:
    authdata = json.load(json_auth_file)
    mysqlHostIP = authdata["badTraktempIns"]["HostIP"]
    mysqlUser = authdata["badTraktempIns"]["User"]
    mysqlPasswd = authdata["badTraktempIns"]["Passwd"]
    mysqlDBName = authdata["badTraktempIns"]["DBName"]

with open('./BackEnds/entryFilters/Utils/dbUtils/dbResponses.json') as json_response_file:
    respodata = json.load(json_response_file)
    connectionErrorMsgMysql = respodata["CNTEResponses"]["connectionErrorMsgMysql"]
    executionCompleteMsg = respodata["CNTEResponses"]["executionCompleteMsg"]


def noTrackerExist(trackerNumber,trackerIP,triggerTime,geoJS):
    try:
        var1 = trackerNumber
        var2 = triggerTime
        var3 = trackerIP
        var4 = " ("+unicode(geoJS['longitude']) +" :: "+ unicode(geoJS['latitude']) +") , "+ unicode(geoJS['city']) +" , "+ unicode(geoJS['region_name']) +" , "+ unicode(geoJS['zip_code']) +" , "+ unicode(geoJS['country_name'])
        # responseNotracker = ":::::" + var1 + ":::" + var2 + "::::::" + var3 + "::::::::" + var4 + ":::::"
        # print responseNotracker
        db1 = MySQLdb.connect(host=mysqlHostIP, user=mysqlUser, passwd=mysqlPasswd, db=mysqlDBName) #AUTHENTICATION TO BE ENCRYPTED AND MOVED OUT SOON 
        #enable MySQL tunnel proxy for security ssh user@host.com -L 9990:localhost:3306
        cursor1 = db1.cursor()
        cursor1.execute ("""INSERT INTO bad_trackers_temp(tracker, TIMESTAMPER, badIP, geoTracker) 
            VALUES ('%s', '%s', '%s', '%s');"""
            % (var1, var2, var3, var4))
        results1 = cursor1.fetchall()
        db1.commit()
        db1.close()
    except MySQLdb.Error:
        print connectionErrorMsgMysql 
        e = MySQLdb
        # print(e.__dict__)
    print executionCompleteMsg
