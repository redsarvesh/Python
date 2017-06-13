#!/usr/bin/python2

import  os,commands,time,sys,socket

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(("",8888))

data=s.recvfrom(100)
data1=s.recvfrom(100)
clientaddr=data[1]

if data[0]=='test' and data1[0]=='123':
	s.sendto('ok',clientaddr)
else:
	s.sendto('wrong username or password',clientaddr)


