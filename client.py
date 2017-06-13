#!/usr/bin/python2

import  os,commands,time,sys,socket

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

s_ip="192.168.10.107"
s_port=8888
print  "Cloud  service  Reloaded  plz enter authentication details  "
time.sleep(2)

s_user=raw_input("enter  user name  :   ")
#  s_user for server user name 

s_password=raw_input("enter  password  : ")
# server password  type here


s.sendto(s_user,(s_ip,s_port))
s.sendto(s_password,(s_ip,s_port))

sdata=s.recvfrom(2)

if   sdata[0]   ==  "ok"  :
	print   "authentication done !! "
	print  "wait for  services  ! "
	time.sleep(2)

else  :
	print    "check your  user and password  "
	exit()







