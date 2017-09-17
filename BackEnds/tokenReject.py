import MySQLdb

def noTokenExist(tokenNumber,tokenIP,triggerTime):
    try:
        var1 = tokenNumber
        var2 = triggerTime
        var3 = tokenIP

        db1 = MySQLdb.connect(host="192.168.1.14", user="mailBot", passwd="umn1234", db="mailBus") #AUTHENTICATION TO BE ENCRYPTED AND MOVED OUT SOON 
        #enable MySQL tunnel proxy for security ssh user@host.com -L 9990:localhost:3306
        cursor1 = db1.cursor()
        cursor1.execute ("INSERT INTO bad_Tokens_temp(token, TIMESTAMPER, badIP) VALUES ('A', 'B', 'C')")
        resultsa = cursor1.fetchall()
        print resultsa
        responseNoToken = "BAD TOKEN ENTRY DETECTED FOR TOKEN NUMBER:: " + tokenNumber + " TRIGGERED AT " + triggerTime + " FROM " + tokenIP 
        print  responseNoToken
        db1.commit()
        db1.close()

    except MySQLdb.Error:
        print "ERROR IN CONNECTION"
        print MySQLdb.Error
    print "Execution completed"


