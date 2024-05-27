#!/usr/bin/python
# -*- coding:utf-8 -*-
import smbus2
import struct
import logging

logging.basicConfig(level=logging.DEBUG)

# this i2c used ups 1.0
ADDRESS = 0x72


def readVoltage(bus):
    try:
        read = bus.read_word_data(ADDRESS, 12) # or input i2c = 2(default ups 1.1), 21, 12, 9
        logging.info("voltage read: " + str(read))
        swapped = struct.unpack("<H", struct.pack(">H", read))[0]
        logging.info("voltage swapped: " + str(swapped))
        voltage = swapped * 1.25 / 1000 / 16
        logging.info("voltage return: " + str(voltage))
        return voltage
    except:
        return 0.0


def readCapacity(bus):
    try:
        read = bus.read_word_data(ADDRESS, 2) # or i2c = 2, 4(default ups 1.1)
        logging.info("capacity read: " + str(read))
        swapped = struct.unpack("<H", struct.pack(">H", read))[0]
        logging.info("capacity swapped: " + str(swapped))
        capacity = swapped / 256
        logging.info("capacity return: " + str(capacity))
        return capacity
    except:
        return 0.0


def QuickStart(bus):
    address = 0x72
    bus.write_word_data(address, 0x06, 0x4000)


def PowerOnReset(bus):
    address = 0x72
    bus.write_word_data(address, 0xfe, 0x0054)


bus = smbus2.SMBus(1)
# PowerOnReset(bus)
QuickStart(bus)

print("Voltage: %5.2fV" % readVoltage(bus))
print("Capacity: %5i%%" % readCapacity(bus))
