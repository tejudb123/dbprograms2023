#Add new column "purpose varchar(50)" to the mobiles table using alter query

import pymysql
con=pymysql.connect(host='bb9iqztcgmcpehmrhljj-mysql.services.clever-cloud.com',user='ubqoiblcfmouazvr',password='86a7IVabYJEvsmUwHdJz',database='bb9iqztcgmcpehmrhljj')
curs=con.cursor()
curs.execute("alter table Mobiles add purpose varchar(50)")
print("New column added")
con.close()