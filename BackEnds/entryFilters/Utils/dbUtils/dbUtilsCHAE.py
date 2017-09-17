#!/usr/bin/python

# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 10:58:26 2017

@author: Sooraj Antony
"""

#Library Import
#System Libraries
import MySQLdb
import json

#UserLibraries


#variableDeclarations
#MysQLAuth centralised delcaration
with open('./BackEnds/entryFilters/Utils/dbUtils/trackerDBConfig.json') as json_auth_file:
    authdata = json.load(json_auth_file)
    mysqlHostIP = authdata["hackClickLogIns"]["HostIP"]
    mysqlHackuser = authdata["hackClickLogIns"]["User"]
    mysqlPasswd = authdata["hackClickLogIns"]["Passwd"]
    mysqlDBName = authdata["hackClickLogIns"]["DBName"]

#MySQL response string decalaration centralised
with open('./BackEnds/entryFilters/Utils/dbUtils/dbResponses.json') as json_response_file:
    respodata = json.load(json_response_file)
    connectionErrorMsgMysql = respodata["CHAEResponses"]["connectionErrorMsgMysql"]
    executionCompleteMsg = respodata["CHAEResponses"]["executionCompleteMsg"]


def hackClickAttemptExist(trackerIP,triggerTime):
    try:
        var1 = trackerIP
        var2 = triggerTime
        dbX = MySQLdb.connect(host=mysqlHostIP, user=mysqlHackuser, passwd=mysqlPasswd, db=mysqlDBName) #AUTHENTICATION TO BE ENCRYPTED AND MOVED OUT SOON 
        #enable MySQL tunnel proxy for security ssh user@host.com -L 9990:localhost:3306
        cursorX = dbX.cursor()
        cursorX.execute (""" INSERT INTO hackClickLog(IPLOG, TIMELOG)
            VALUES ('%s', '%s') """ 
            % (var1, var2))
        resultsX = cursorX.fetchall()
        dbX.commit()
        dbX.close()
    except MySQLdb.Error:
        print connectionErrorMsgMysql 
        print MySQLdb.Error
    print executionCompleteMsg
 
