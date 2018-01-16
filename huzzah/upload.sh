#!/bin/bash
set -x
esptool.py --port /dev/cu.SLAB_USBtoUART erase_flash
esptool.py -p /dev/cu.SLAB_USBtoUART --baud 460800 write_flash --flash_size=detect 0 firmware-combined.bin
sleep 5
ampy -p /dev/cu.SLAB_USBtoUART put adafruit_ssd1306.py
ampy -p /dev/cu.SLAB_USBtoUART put adafruit_bus_device
ampy -p /dev/cu.SLAB_USBtoUART put register
ampy -p /dev/cu.SLAB_USBtoUART put main.py
ampy -p /dev/cu.SLAB_USBtoUART put screen.py
