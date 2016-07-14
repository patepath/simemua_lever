#! /usr/bin/env python

import socket
import smbus
import time

in_addr = 0x20
reg_addr = 0x12

a2d_addr = 0x6a
a2d_ch = 0xB8
bus = smbus.SMBus(1)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('192.168.1.10', 2510))

#display_serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#display_serv.connect(('192.168.1.42', 55555))

old_sent = 'D215'

while True:

	try:
		value = bus.read_byte_data(in_addr, reg_addr)


		if value == 0xff:
			pos = "0"

		elif value & 0x01 == 0x00:
			pos = "D"

		elif value & 0x04 == 0x00:
			pos = "EB"


		elif value & 0x02 == 0x00:
			pos = "B"

		if value & 0x08 == 0x00:
			dm = 1

		else:
			dm = 0

		value = bus.read_word_data(a2d_addr, a2d_ch)
		duty = float((value & 0xff) << 8 | value >> 8)
		#raw_duty = duty

		if duty > 21500:
			duty = ((duty-21500)/7781) * 100
	
			if duty < 0:
				duty = 0

			if duty > 100:
				duty = 100

		elif duty < 14500:
			duty = ((14500 - duty)/12840) * -100

			if duty < -100:
				duty = -100

		else :
			duty = 0


		sent = str("D215 %d %s %d\n" % (duty, pos, dm))

		if sent != old_sent:
			s.send(sent)
			old_sent = sent

		time.sleep(0.10)

	except KeyboardInterrupt:
		s.close()
		#display_serv.close()
		break

