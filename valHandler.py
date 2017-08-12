# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 10:58:26 2017

@author: Sooraj Antony
"""



#system functions
from datetime import datetime 

#user functions
from hashingFunction import hasher

def importData(genTime,mailIDHolder,usernameHolder):
	viff = dict();
	viff['emailID']  = mailIDHolder
	viff['username']  = usernameHolder
	###############tempMOCKER###############
	# viff['emailID']  = "asdasd"
	# viff['username']  = "asdasd"
	###############tempMOCKER###############
	viff['accessedTime'] = genTime.strftime('%Y-%m-%d %H:%M:%S')
	formGenTime = genTime.strftime('%Y-%m-%d %H:%M:%S::%f')
	viff['formID'] = hasher(formGenTime)
	return(viff)


 
def tokenizer(saltedEmailID,saltedUsername,formID):
    tokGen = dict();
    rawtoken = str(saltedEmailID)+str(saltedUsername)
    tokenInit = hasher(rawtoken)+str(formID)
    temptoken = str(tokenInit)+str(formID)
    tokGen['tokenID'] = temptoken
    return(tokGen)




def redirector(redirURL):
	#time.sleep(0.1)
	print "<meta http-equiv=\"refresh\" content=\"5; url=http://microsoft.com/";

