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
    mysqlHostIP = authdata["TonStatHlrUpd"]["HostIP"]
    mysqlUser = authdata["TonStatHlrUpd"]["User"]
    mysqlPasswd = authdata["TonStatHlrUpd"]["Passwd"]
    mysqlDBName = authdata["TonStatHlrUpd"]["DBName"]

with open('./BackEnds/entryFilters/Utils/dbUtils/dbResponses.json') as json_response_file:
    respodata = json.load(json_response_file)
    connectionErrorMsgMysql = respodata["VUAResponses"]["connectionErrorMsgMysql"]
    executionCompleteMsg = respodata["VUAResponses"]["executionCompleteMsg"]



def valueUpdateAppender(varA, varB):
    try:
        dbA = MySQLdb.connect(host=mysqlHostIP, user=mysqlUser, passwd=mysqlPasswd, db=mysqlDBName) #enable MySQL tunnel proxy for security ssh user@host.com -L 9990:localhost:3306
        cursorA = dbA.cursor()
        
        cursorA.execute (""" 
            SELECT %s 
            FROM tokenStatusHandler 
            WHERE token = '%s'
            """ 
            % (varA , varB)
            )
        outValues = cursorA.fetchone()
        outValue =  outValues[0]
        dbA.close
        return(outValue)
    except MySQLdb.Error:
        print connectionErrorMsgMysql 
        print MySQLdb.Error
    print executionCompleteMsg