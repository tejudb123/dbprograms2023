#program to accept modelname, search mobile in the table, show the mobile details if found else display "not found" message

import pymysql
con=pymysql.connect(host='bb9iqztcgmcpehmrhljj-mysql.services.clever-cloud.com',user='ubqoiblcfmouazvr',password='86a7IVabYJEvsmUwHdJz',database='bb9iqztcgmcpehmrhljj')
curs=con.cursor()

modelnm=input("Enter Model name : ")
curs.execute("select * from Mobiles where modelnm='%s'" %modelnm)
data=curs.fetchone()

if data:
    print(data)
else:
    print("Data not found")

con.close()