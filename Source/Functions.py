# coding: UTF-8
import time

__author__ = 'nonakanaoki'

delayval = 0.6
delayval2 = 2


def get_chip(var):
    var.write(b'A0X0Y0Z200')
    time.sleep(delayval)
    var.write(b'A0X-108Y-46Z200')
    time.sleep(delayval)
    var.write(b'A0X-108Y-46Z60')
    time.sleep(delayval)
    var.write(b'A0X-108Y-46Z48')
    time.sleep(delayval)
    var.write(b'A0X-108Y-46Z200')
    time.sleep(delayval)


def get_reagent(var):
    var.write(b'A0X-40Y-120Z200')
    time.sleep(delayval)
    var.write(b'A0X-40Y-120Z20')
    time.sleep(delayval)
    var.write(b'p5')
    time.sleep(delayval2)
    var.write(b'A0X-40Y-120Z200')
    time.sleep(delayval)


def set_reagent(var):
    var.write(b'A0X-28Y117Z200')
    time.sleep(delayval)
    var.write(b'A0X-28Y117Z140')
    time.sleep(delayval)
    var.write(b'd')
    time.sleep(delayval2)
    var.write(b'A0X-28Y117Z200')
    time.sleep(delayval)


def put_chip(var):
    var.write(b'A0X85Y155Z200')
    time.sleep(delayval)
    var.write(b'e')
    time.sleep(delayval)


def go_home(var):
    var.write(b'A0X0Y0Z200')
    time.sleep(delayval)
    var.write(b'h')

