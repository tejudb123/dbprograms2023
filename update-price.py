#Program to accept prodid & new price and update price inthe mobile data in the table if found else display "mobile does notexist

import pymysql
con=pymysql.connect(host='bb9iqztcgmcpehmrhljj-mysql.services.clever-cloud.com',user='ubqoiblcfmouazvr',password='86a7IVabYJEvsmUwHdJz',database='bb9iqztcgmcpehmrhljj')
curs=con.cursor()

prodid=int(input("Enter Mobile prodid : "))
curs.execute("select * from Mobiles where prodid=%d"%prodid)
data=curs.fetchone()

if data:
    print(data)
    price=float(input("Enter new price : "))
    curs.execute("update Mobiles set price=%.2f where prodid=%d"%(price,prodid))
    con.commit()
    print("Price updated successfully")
else:
    print("Mobile does not exist")

con.close()