#!/usr/bin/python

# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 10:58:26 2017

@author: Sooraj Antony
"""


#System libraries
from datetime import datetime
import time
import cgi, cgitb 


#UserCustom libraries
from hashingFunction import hasher
from hashingFunction import salter

from valHandler import tokenizer
from valHandler import redirector
from valHandler import importData

def controller():
	global genTime
	genTime = datetime.now()




def importForm():
	form = cgi.FieldStorage() # Create instance of FieldStorage 
	mailIDHolder  = form.getvalue('emailIDs')
	usernameHolder  = form.getvalue('username')
	###############tempMOCKER###############
	# viff['emailID']  = "asdasd"
	# viff['username']  = "asdasd"
	###############tempMOCKER###############
	viff = importData(genTime,mailIDHolder,usernameHolder)
	return(viff)




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
	print "<h6>Time triggered: %s </h6>" % (accessedTime)
	print "Result: <br> <h1>Mail to %s to mail ID %s with form %s with token ID %s was opened at %s</h1>" % (username,emailID,formID,tokenID,accessedTime)
	print "</body>"
	print "</html>"
 	redirURL="google.com"
	redirector(redirURL)
	
 
     
 


#Main Function initiator
controller()

das = importForm()
locals().update(das)

sltra = salter(emailID,username)
locals().update(sltra)

tgenera = tokenizer(saltedEmailID,saltedUsername,formID)
locals().update(tgenera)

responsePreview() #TO BE REMOVED
#responseHandler()




