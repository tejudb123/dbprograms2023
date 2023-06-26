#program to display group by information - brand, total models under the company, average price and average rating

import pymysql
con=pymysql.connect(host='bb9iqztcgmcpehmrhljj-mysql.services.clever-cloud.com',user='ubqoiblcfmouazvr',password='86a7IVabYJEvsmUwHdJz',database='bb9iqztcgmcpehmrhljj')
curs=con.cursor()

brand=input("Enter brand of the mobile : ")
curs.execute("select company , count(modelnm), avg(price), avg(rating) from Mobiles where company='%s'"%brand)
data=curs.fetchall()
print(data)
con.close()

