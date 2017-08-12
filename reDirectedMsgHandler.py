#!/usr/bin/python

# Import modules for CGI handling 
import cgi, cgitb 
from hashingFunction import hasher
from datetime import datetime


#input values from response form
def valueImportFromForm():
	viff = dict();
	# form = cgi.FieldStorage() # Create instance of FieldStorage 
	# viff['emailID']  = form.getvalue('emailIDs')
	# viff['username']  = form.getvalue('username')
	# viff['time'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
	# viff['formGenTime'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S::%f')
	# viff['formID'] = hasher(formGenTime)
	#############temoMOCKER###############
	viff['emailID']  = "asdasd"
	viff['username']  = "asdasd"
	viff['time'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
	formGenTime = datetime.now().strftime('%Y-%m-%d %H:%M:%S::%f')
	viff['formID'] = hasher(formGenTime)
	return(viff)

#salterForTokenGeneration
def salter():
	sltr = dict();
	tempemailID = hasher("emailID")
	tempusername = hasher("username")
	sltr['saltedEmailID'] = tempemailID
	sltr['saltedUsername'] = tempusername
	return(sltr)

def tokenGenerator(saltedUsername,formID):
    tokGen = dict();
    rawtoken = str(saltedEmailID)+str(saltedUsername)
    tokenInit = hasher(rawtoken)+str(formID)
    temptoken = str(tokenInit)+str(formID)
    tokGen['token'] = temptoken
    return(tokGen)



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
das = valueImportFromForm()
locals().update(das)

sltra = salter()
locals().update(sltra)

tgenera = tokenGenerator(saltedUsername,formID)
locals().update(tgenera)

responsePreview() #TO BE REMOVED
#responseHandler()




