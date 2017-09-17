#!/usr/bin/python

# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 10:58:26 2017

@author: Sooraj Antony
"""

#System Libraries
import MySQLdb
import json
import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )


#UserLibraries
from valHandler import location
from dbUtilsTE import tokenExist
from dbUtilsNTE import noTokenExist


#variableDeclarations
with open('./BackEnds/entryFilters/Utils/dbUtils/trackerDBConfig.json') as json_auth_file:
    authdata = json.load(json_auth_file)
    mysqlHostIP = authdata["selectTSHuser"]["HostIP"]
    mysqlUser = authdata["selectTSHuser"]["User"]
    mysqlPasswd = authdata["selectTSHuser"]["Passwd"]
    mysqlDBName = authdata["selectTSHuser"]["DBName"]

with open('./BackEnds/entryFilters/Utils/dbUtils/dbResponses.json') as json_response_file:
    respodata = json.load(json_response_file)
    connectionErrorMsgMysql = respodata["TSCResponses"]["connectionErrorMsgMysql"]
    executionCompleteMsg = respodata["TSCResponses"]["executionCompleteMsg"]


def dbTokenStatusChecker(tokenNumber,tokenIP,triggerTime):
    try:
        geoJS = location(tokenIP)
        db = MySQLdb.connect(host=mysqlHostIP, user=mysqlUser, passwd=mysqlPasswd, db=mysqlDBName) #enable MySQL tunnel proxy for security ssh user@host.com -L 9990:localhost:3306
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
            #SCRIPT TO LOG location and other details
            tokenExist(tokenNumber,tokenIP,triggerTime,geoJS)
        else:
            noTokenExist(tokenNumber,tokenIP,triggerTime,geoJS)
    except MySQLdb.Error:
        print connectionErrorMsgMysql 
        print MySQLdb.Error
    print executionCompleteMsg
