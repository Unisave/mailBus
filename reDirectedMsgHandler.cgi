#!/usr/bin/python

# Import modules for CGI handling 
import cgi, cgitb 
from datetime import datetime


# Create instance of FieldStorage 
form = cgi.FieldStorage() 

# Get data from fields

def responseHandler():
	tokenID = form.getvalue('token')
	formID = form.getvalue('formIDs')
	emailID  = form.getvalue('emailIDs')
	username  = form.getvalue('username')
	time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

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


def main():
    responseHandler()