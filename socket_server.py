#! /usr/bin/env python

import socket
import time

host = ''
port = 2515

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, port))
s.listen(1)

while True:
	conn, addr = s.accept()

	while True:
		data = conn.recv(16)
		if data:
			print 'hello ' + data
		else:
			break

s.close()


