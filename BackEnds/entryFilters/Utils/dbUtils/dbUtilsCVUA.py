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
    mysqlHostIP = authdata["TrakStatHlrSel"]["HostIP"]
    mysqlUser = authdata["TrakStatHlrSel"]["User"]
    mysqlPasswd = authdata["TrakStatHlrSel"]["Passwd"]
    mysqlDBName = authdata["TrakStatHlrSel"]["DBName"]
    mysqlTabName = authdata["TrakStatHlrSel"]["TabName"]

with open('./BackEnds/entryFilters/Utils/dbUtils/dbResponses.json') as json_response_file:
    respodata = json.load(json_response_file)
    connectionErrorMsgMysql = respodata["CVUAResponses"]["connectionErrorMsgMysql"]
    executionCompleteMsg = respodata["CVUAResponses"]["executionCompleteMsg"]



def valueClickUpdateAppender(varA, varB):
    try:
        dbA = MySQLdb.connect(host=mysqlHostIP, user=mysqlUser, passwd=mysqlPasswd, db=mysqlDBName) #enable MySQL tunnel proxy for security ssh user@host.com -L 9990:localhost:3306
        cursorA = dbA.cursor()
        
        cursorA.execute (""" 
            SELECT %s 
            FROM %s 
            WHERE tracker = '%s'
            """ 
            % (varA, mysqlTabName, varB)
            )
        outValues = cursorA.fetchone()
        outValue =  outValues[0]
        dbA.close
        return(outValue)
    except MySQLdb.Error:
        print connectionErrorMsgMysql 
        print MySQLdb.Error
    print executionCompleteMsg