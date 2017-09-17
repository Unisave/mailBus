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
    mysqlHostIP = authdata["badTontempIns"]["HostIP"]
    mysqlUser = authdata["badTontempIns"]["User"]
    mysqlPasswd = authdata["badTontempIns"]["Passwd"]
    mysqlDBName = authdata["badTontempIns"]["DBName"]

with open('./BackEnds/entryFilters/Utils/dbUtils/dbResponses.json') as json_response_file:
    respodata = json.load(json_response_file)
    connectionErrorMsgMysql = respodata["NTEResponses"]["connectionErrorMsgMysql"]
    executionCompleteMsg = respodata["NTEResponses"]["executionCompleteMsg"]


def noTokenExist(tokenNumber,tokenIP,triggerTime,geoJS):
    try:
        var1 = tokenNumber
        var2 = triggerTime
        var3 = tokenIP
        var4 = " ("+unicode(geoJS['longitude']) +" :: "+ unicode(geoJS['latitude']) +") , "+ unicode(geoJS['city']) +" , "+ unicode(geoJS['region_name']) +" , "+ unicode(geoJS['zip_code']) +" , "+ unicode(geoJS['country_name'])
        db1 = MySQLdb.connect(host=mysqlHostIP, user=mysqlUser, passwd=mysqlPasswd, db=mysqlDBName) #AUTHENTICATION TO BE ENCRYPTED AND MOVED OUT SOON 
        #enable MySQL tunnel proxy for security ssh user@host.com -L 9990:localhost:3306
        cursor1 = db1.cursor()
        cursor1.execute (""" INSERT INTO bad_Tokens_temp(token, TIMESTAMPER, badIP, geoTracker) 
            VALUES ('%s', '%s', '%s', '%s') """
             % (var1, var2, var3, var4))
        results1 = cursor1.fetchall()
        db1.commit()
        db1.close()
        responseNoToken = "BAD TOKEN ENTRY DETECTED FOR TOKEN NUMBER:: " + tokenNumber + " TRIGGERED AT " + triggerTime + " FROM " + tokenIP 
    except MySQLdb.Error:
        print connectionErrorMsgMysql 
        print MySQLdb.Error
    print executionCompleteMsg
