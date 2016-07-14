#! /usr/bin/env python

import socket
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('192.168.1.38', 55555))
i = 0

for i in range(1, 10):
	sock.send("hello" + str(i) + "\n")
	time.sleep(1)

sock.close()

