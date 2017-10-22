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
from dbUtilsCTE import trackerExist
from dbUtilsCNTE import noTrackerExist


#variableDeclarations
with open('./BackEnds/entryFilters/Utils/dbUtils/trackerDBConfig.json') as json_auth_file:
    authdata = json.load(json_auth_file)
    mysqlHostIP = authdata["tempTrakMapSel"]["HostIP"]
    mysqlUser = authdata["tempTrakMapSel"]["User"]
    mysqlPasswd = authdata["tempTrakMapSel"]["Passwd"]
    mysqlDBName = authdata["tempTrakMapSel"]["DBName"]
    mysqlTabName = authdata["tempTrakMapSel"]["TabName"]

with open('./BackEnds/entryFilters/Utils/dbUtils/dbResponses.json') as json_response_file:
    respodata = json.load(json_response_file)
    connectionErrorMsgMysql = respodata["CTSUResponses"]["connectionErrorMsgMysql"]
    executionCompleteMsg = respodata["CTSUResponses"]["executionCompleteMsg"]


def dbTrackerStatusUpdator(trackerNumber,trackerIP,triggerTime):
    try:
        geoJS = location(trackerIP)
        db = MySQLdb.connect(host=mysqlHostIP, user=mysqlUser, passwd=mysqlPasswd, db=mysqlDBName) #enable MySQL tunnel proxy for security ssh user@host.com -L 9990:localhost:3306
        cursor = db.cursor()
        cursor.execute ("""
                 SELECT tracker 
                 FROM %s
                 WHERE tracker = '%s'
               """ 
               % (mysqlTabName, trackerNumber)
        )
        results = cursor.fetchall()
        db.close()
        # Check if anything at all is returned
        if results:
            #SCRIPT TO LOG location and other details
            trackerExist(trackerNumber,trackerIP,triggerTime,geoJS)
        else:
            noTrackerExist(trackerNumber,trackerIP,triggerTime,geoJS)
    except MySQLdb.Error:
        print connectionErrorMsgMysql 
        print MySQLdb.Error
    print executionCompleteMsg
