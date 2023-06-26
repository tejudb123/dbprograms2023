# program to accept ram and rom, display list of mobiles of the ram-rom storage space combination

import pymysql
con=pymysql.connect(host='bb9iqztcgmcpehmrhljj-mysql.services.clever-cloud.com',user='ubqoiblcfmouazvr',password='86a7IVabYJEvsmUwHdJz',database='bb9iqztcgmcpehmrhljj')
curs=con.cursor()

ram=int(input("Enter the RAM : "))
rom=int(input("Enter the ROM : "))

curs.execute("select ram, rom, modelnm from Mobiles where ram=%d and rom=%d"%(ram,rom))
data=curs.fetchall()
print(data)
con.close()