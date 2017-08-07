
import pymysql

# URL DATA 
input = []  ## LIST OF LISTS
#IDlist = test1
for id in IDlist:
     url='www.example.com/'+str(id)
     values=requests.get(url) ##some parse omitted
     input.append([values[1],values[2],id])

# DATABASE UPDATE
connection = pymysql.connect(
            host='localhost', db='test_db',
            user='root', passwd='***')
mycursor = connection.cursor()

for items in input:
     sql="""UPDATE mytable
         SET COL1=%s, COL2=%s
         WHERE ID=%s"""
     mycursor.execute(sql, tuple(items))    
     connection.commit() 

mycursor.close()  ## here all loops done
connection.close()  ## close db connection