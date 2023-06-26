#program to take new mobile data as input and add mobile to the DB table

import pymysql
con=pymysql.connect(host='bb9iqztcgmcpehmrhljj-mysql.services.clever-cloud.com',user='ubqoiblcfmouazvr',password='86a7IVabYJEvsmUwHdJz',database='bb9iqztcgmcpehmrhljj')
curs=con.cursor()

prodid=int(input("Enter new mobile ID : "))
modelnm=input("Enter model name : ")
company=input("Enter Company : ")
connectivity=input("Enter connectivity : ")
ram=int(input("Enter RAM : "))
rom=int(input("Enter ROM : "))
color=input("Enter Color : ")
screen=input("Enter screen size : ")
battery=input("Enter Battery : ")
proccessor=input("Enter Processor : ")
price=float(input("Enter Price : "))
rate=float(input("Rate : "))

try:
    curs.execute("insert into Mobiles values (%d,'%s','%s','%s',%d,%d,'%s','%s','%s','%s',%.2f,%.2f)"%(prodid,modelnm,company,connectivity,ram,rom,color,screen,battery,proccessor,price,rate))
    con.commit()
    print("One data added successfully")
except:
    print("Can't insert data")

con.close()


