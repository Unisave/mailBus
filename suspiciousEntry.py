#!/usr/bin/python

# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 10:58:26 2017

@author: Sooraj Antony
"""


import sys
import re

from dbUtils import hackAttemptExist
from datetime import datetime

rawip = sys.argv[1]
rawtriggertime = sys.argv[2]




# #write to file
# f = open('tempBuffer.file', 'a')
# f.write('\n The ip is ')  
# f.write(ip)  
# f.write('\n The token is ')  
# f.write(token)
# f.close()

def finalIPSanitizer(ip):
	if re.match("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", ip) is not None:
		inputtableIP = ip
	else:
		renderedIP = re.sub('[^\w\s\.]', '', ip)
		inputtableIP = "Problematic IP : " + renderedIP
	return inputtableIP


def finalTimeSanitizer(triggertime):
	if re.match("\d{4}\-\d{2}\-\d{2}\:\:\d{2}\:\d{2}\:\d{2}", triggertime) is not None:
		inputtableTimeTrigger = triggertime
	else:
		generTime = datetime.now()
		formGenTime = generTime.strftime('%Y-%m-%d::%H:%M:%S')
		renderedIP = re.sub('[^\w\s\:\-]', '', triggertime)
		inputtableTimeTrigger = "PT:: " + renderedIP + "  ATG:: " + formGenTime
	return inputtableTimeTrigger

#DbPrint
finalip =  finalIPSanitizer(rawip)
finalTime = finalTimeSanitizer(rawtriggertime)
hackAttemptExist(finalip , finalTime)
