#program to accept company like "samsung" and display list of mobiles of that category in the ascending order of price

import pymysql
con=pymysql.connect(host='bb9iqztcgmcpehmrhljj-mysql.services.clever-cloud.com',user='ubqoiblcfmouazvr',password='86a7IVabYJEvsmUwHdJz',database='bb9iqztcgmcpehmrhljj')
curs=con.cursor()
data=curs.execute("select * from Mobiles where company='Samsung' order by price")
data=curs.fetchall()
print(data)
con.close()
