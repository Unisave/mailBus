#!/usr/bin/python

# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 10:58:26 2017

@author: Sooraj Antony
"""


#System libraries
from datetime import datetime

#UserCustom libraries
from hashingFunction import hasher
from hashingFunction import salter
from valHandler import importForm
from valHandler import tokenizer


def controller():
	global formGenTime
	GenTime = datetime.now()


def responsePreview():	
	print "Content-type:text/html\r\n\r\n"
	print "<html>"
	print "<head>"
	print "<title>Hello - Second CGI Program</title>"
	print "</head>"
	print "<body>"
	print "<h6>token triggered: %s </h6>" % (tokenID)
	print "<h6>token form bind ID: %s </h6>" % (formID)
	print "<h6>mailOriginForToken: %s </h6>" % (emailID)
	print "<h6>Username: %s </h6>" % (username)
	print "<h6>Time triggered: %s </h6>" % (time)
	print "Result: <br> <h1>Mail to %s to mail ID %s with form %s with token ID %s was opened at %s</h1>" % (username,emailID,formID,tokenID,time)
	print "</body>"
	print "</html>"



#Main Function initiator
das = importForm(formGenTime)
locals().update(das)

sltra = salter(emailID,username)
locals().update(sltra)

tgenera = tokenGenerator(saltedUsername,formID)
locals().update(tgenera)

responsePreview() #TO BE REMOVED
#responseHandler()




