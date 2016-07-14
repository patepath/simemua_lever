#! /usr/bin/env python

import socket
import smbus
import time

a2d_addr = 0x6a
a2d_ch = 0xB8

bus = smbus.SMBus(1)

while(True):
	value = bus.read_word_data(a2d_addr, a2d_ch)
	duty = float((value & 0xff) << 8 | value >> 8)
	raw_duty = duty
	duty = ((duty-21500)/7781) * 100
	
	if duty < 0:
		duty = 0

	if duty > 100:
		duty = 100

	print str(100-duty)
	s = socket.socket()
	s.connect(('192.168.1.42', 2515))
	s.send("%.2f" %(100-duty))
	s.close()
	
	time.sleep(1)


