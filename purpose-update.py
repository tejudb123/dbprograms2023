#program to accept modelname and purpose, update all mobiles of the model with the purpose ( gaming/office/social, etc.)

import pymysql
con=pymysql.connect(host='bb9iqztcgmcpehmrhljj-mysql.services.clever-cloud.com',user='ubqoiblcfmouazvr',password='86a7IVabYJEvsmUwHdJz',database='bb9iqztcgmcpehmrhljj')
curs=con.cursor()

modelnm=input("Enter model name : ")
curs.execute("select * from Mobiles where modelnm='%s'"%modelnm)
data=curs.fetchone()
if data:
    print(data)
    purpose=input("Enter the purpose : ")
    curs.execute("update Mobiles set purpose='%s' where modelnm='%s'"%(purpose,modelnm))
    data1=curs.fetchone()
    print(data1)
    con.commit()
    print("Purpose of the Mobile updated sucessfully")
else:
    print("Mobile doen not found")
con.close()