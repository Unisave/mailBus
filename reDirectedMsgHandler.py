#!/usr/bin/python

# Import modules for CGI handling 
import cgi, cgitb 
from hashingFunction import hasher
from datetime import datetime


#input values from response form
def valueImportFromForm():
	form = cgi.FieldStorage() # Create instance of FieldStorage 
	emailID  = form.getvalue('emailIDs')
	username  = form.getvalue('username')
	time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
	formGenTime = datetime.now().strftime('%Y-%m-%d %H:%M:%S::%f')
	formID = hasher(formGenTime)


#salterForTokenGeneration
def salter():
	saltedEmailID = hasher(emailID)
	saltedUsername = hasher(email)

def tokenGenerator():
    rawtoken = str(saltedEmailID)+str(saltedUsername)
    tokenInit = salter(rawtoken)+str(formID)
    token = str(tokenInit)+str(formID)




def responsePreview():
	
	print "Content-type:text/html\r\n\r\n"
	print "<html>"
	print "<head>"
	print "<title>Hello - Second CGI Program</title>"
	print "</head>"
	print "<body>"
	print "<h6>token triggered: %s </h6>" % (token)
	print "<h6>token form bind ID: %s </h6>" % (formID)
	print "<h6>mailOriginForToken: %s </h6>" % (emailID)
	print "<h6>Username: %s </h6>" % (username)
	print "<h6>Time triggered: %s </h6>" % (time)
	print "Result: <br> <h1>Mail to %s to mail ID %s with form %s with token ID %s was opened at %s</h1>" % (username,emailID,formID,tokenID,time)
	print "</body>"
	print "</html>"



#Main Function initiator
def moduleCaller():
	valueImportFromForm()
	salter()
	tokenGenerator()
	responsePreview() #TO BE REMOVED
	#responseHandler()


moduleCaller()