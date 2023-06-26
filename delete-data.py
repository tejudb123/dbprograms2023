#program to accept prodid, display the mobile data and ask "Do you want to delete?" if "yes" delete the mobile from the table
import pymysql
con=pymysql.connect(host='bb9iqztcgmcpehmrhljj-mysql.services.clever-cloud.com',user='ubqoiblcfmouazvr',password='86a7IVabYJEvsmUwHdJz',database='bb9iqztcgmcpehmrhljj')
curs=con.cursor()

prodid=int(input("Enter mobile prodid : "))
curs.execute("select * from Mobiles where prodid=%d"%prodid)
data=curs.fetchone()

if data:
    print(data)
    ch=input("Do you really want to delete? (Yes/No) : ")
    if ch=='Yes':
        curs.execute("delete from Mobiles where prodid='%s'"%ch)
        con.commit()
        print("Data deleted successfully")
    else:
        print("Deletion Cancelled")
else:
    print("Mobile does not exist")
con.close()
