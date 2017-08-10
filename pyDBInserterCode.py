import cgi, cgitb 
from datetime import datetime
import pymysql


# DATABASE UPDATE
connection = pymysql.connect(
            host='localhost', db='admin_logger',
            user='root', passwd='careersnow@123')
mycursor = connection.cursor()



##MYSQL Sscript to WRITE to mysql db
##     sql="""SCRIPT TO PERFORM WRITES"""
##     mycursor.execute(sql)    
##     connection.commit() 





    print "Content-type:text/html\r\n\r\n"
    print "<html>"
    print "<head>"
    print "<title>Hello - Second CGI Program</title>"
    print "</head>"
    print "<body>"
    sql="""SHOW TABLES;"""
    for result in cursor.execute(sql, multi=True):
      if result.with_rows:
        print("<h6>Rows produced by statement '{}':</h6>".format(
          result.statement))
        print("<h6>"result.fetchall()"</h6>")
      else:
        print("<h6>Number of rows affected by statement '{}': {}</h6>".format(
          result.statement, result.rowcount))
    print "</body>"
    print "</html>"







mycursor.close()  ## here all loops done
connection.close()  ## close db connection