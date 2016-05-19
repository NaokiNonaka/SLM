# coding: UTF-8

import serial
from Source.Functions import *
import sys

module_Path = sys.argv[1]
ser = serial.Serial(module_Path, 9600)
# ser = serial.Serial('/dev/tty.usbmodem1411', 9600)


if __name__ == '__main__':
    while True:
        inp = input('command\n')
        if inp in '1':
            get_chip(ser)
        elif inp in '2':
            get_reagent(ser)
        elif inp in '3':
            set_reagent(ser)
        elif inp in '4':
            put_chip(ser)
        elif inp in '5':
            get_chip(ser)
            get_reagent(ser)
            set_reagent(ser)
            put_chip(ser)
            go_home(ser)
        elif inp in '0':
            break
        elif inp in 'h':
            go_home(ser)

    ser.close()
