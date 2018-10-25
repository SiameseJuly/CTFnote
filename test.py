#!/usr/bin/python
# -*- coding: UTF-8 -*-
# filename：server.py

import socket               

s = socket.socket()         
host = socket.gethostname() 
port = 12345                
s.bind((host, port))        

s.listen(5)                 
while True:
    c, addr = s.accept()    
    print 'addr：', addr
    c.send('welcom')
    c.close()                
