#! /usr/bin/env python

import smbus
import time

a2d_addr = 0x6a
a2d_ch = 0xB8

bus = smbus.SMBus(1)

while(True):
	value = bus.read_word_data(a2d_addr, a2d_ch)
	print (value & 0xff) << 8 | value >> 8
	time.sleep(1)


