#!/usr/bin/python
import  cgi,cgitb
import MySQLdb as mariadb
db=mariadb.connect('127.0.0.1','root','redhat','adhoc')
cursor=db.cursor()
cgitb.enable()
print  "content-type:text/html"
print  ""

x=cgi.FieldStorage()
nm=x.getvalue('name')
passwd=x.getvalue('pwd')
sql="""select name,password from info"""
cursor.execute(sql)
flag=0;
for name,password in cursor:
	if  nm == name and passwd == password:
		flag=1;
		break;
	
	elif nm!=name or passwd!=password:
		flag=0;

if flag==1:
	print "<META HTTP-EQUIV='refresh' content='0; url=http://192.168.122.1/final_sec.html'>"

elif flag==0:
	print "<META HTTP-EQUIV='refresh' content='0; url=http://192.168.122.1/final.html'/>"	


