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
#MysQLAuth centralised delcaration
with open('./BackEnds/entryFilters/Utils/dbUtils/trackerDBConfig.json') as json_auth_file:
    authdata = json.load(json_auth_file)
    mysqlHostIP = authdata["hackLogIns"]["HostIP"]
    mysqlHackuser = authdata["hackLogIns"]["User"]
    mysqlPasswd = authdata["hackLogIns"]["Passwd"]
    mysqlDBName = authdata["hackLogIns"]["DBName"]
    mysqlTabName = authdata["hackLogIns"]["TabName"]

#MySQL response string decalaration centralised
with open('./BackEnds/entryFilters/Utils/dbUtils/dbResponses.json') as json_response_file:
    respodata = json.load(json_response_file)
    connectionErrorMsgMysql = respodata["HAEResponses"]["connectionErrorMsgMysql"]
    executionCompleteMsg = respodata["HAEResponses"]["executionCompleteMsg"]


def hackAttemptExist(tokenIP,triggerTime):
    try:
        var1 = tokenIP
        var2 = triggerTime
        dbX = MySQLdb.connect(host=mysqlHostIP, user=mysqlHackuser, passwd=mysqlPasswd, db=mysqlDBName) #AUTHENTICATION TO BE ENCRYPTED AND MOVED OUT SOON 
        #enable MySQL tunnel proxy for security ssh user@host.com -L 9990:localhost:3306
        cursorX = dbX.cursor()
        cursorX.execute (""" INSERT INTO %s(IPLOG, TIMELOG)
            VALUES ('%s', '%s') """ 
            % (mysqlTabName, var1, var2))
        resultsX = cursorX.fetchall()
        dbX.commit()
        dbX.close()
    except MySQLdb.Error:
        print connectionErrorMsgMysql 
        print MySQLdb.Error
    print executionCompleteMsg
 
