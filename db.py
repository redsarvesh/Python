#!/usr/bin/python
import  cgi,cgitb
import MySQLdb as mariadb
db=mariadb.connect('127.0.0.1','root','redhat','adhoc')
cursor=db.cursor()
cgitb.enable()
print  "content-type:text/html"
print  ""

x=cgi.FieldStorage()
f_name=x.getvalue('first_name')
l_name=x.getvalue('last_name')

sql="""insert into info(first_name,last_name)values('"""+f_name+"""','"""+l_name+"""')"""

try:
        cursor.execute(sql)
        db.commit()
except:
        db.rollback()

db.close()

