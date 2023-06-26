#Take field as an input like rom and display all mobiles in the descending order of the that field.

import pymysql
con=pymysql.connect(host='bb9iqztcgmcpehmrhljj-mysql.services.clever-cloud.com',user='ubqoiblcfmouazvr',password='86a7IVabYJEvsmUwHdJz',database='bb9iqztcgmcpehmrhljj')
curs=con.cursor()

rom=int(input("Enter size of rom : "))
curs.execute("select modelnm, rom from Mobiles where rom=%d order by modelnm desc"%rom)
data=curs.fetchall()
print(data)

con.close()