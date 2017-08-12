# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 10:58:26 2017

@author: Sooraj Antony
"""

#system modules
import hashlib

#hash Generator module
def hasher(subber):
	hash_object = hashlib.sha512(subber)
	hex_dig = hash_object.hexdigest()
	return(hex_dig)
 
 
#Salter For TokenGeneration 
def salter(emailID,username):
	sltr = dict();
	tempemailID = hasher(emailID)
	tempusername = hasher(username)
	sltr['saltedEmailID'] = tempemailID
	sltr['saltedUsername'] = tempusername
	return(sltr)
