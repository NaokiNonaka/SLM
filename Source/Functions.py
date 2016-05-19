# coding: UTF-8
import time

__author__ = 'nonakanaoki'


delayval = 1
delayval2 = 1.7


def wait_end(var):
    while 1:
        if var.inWaiting() > 0:
            data = var.read(var.inWaiting())
            print(data)
            if data.find(b".."):
                print("OK")
                break


def command_write(var1,var2):
    var1.write(var2)
    wait_end(var1)
    # time.sleep(0.3)


def get_chip(var):
    command_write(var,b'A0X0Y0Z150')
    command_write(var,b'A0X-108Y-46Z150')

    command_write(var,b'A0X-108Y-46Z60')
    time.sleep(delayval)
    command_write(var,b'A0X-108Y-46Z48')
    command_write(var,b'A0X-108Y-46Z150')


def get_reagent(var):

    command_write(var,b'A0X-40Y-120Z150')
    command_write(var,b'A0X-40Y-120Z50')
    time.sleep(delayval2)
    command_write(var,b'p5')
    time.sleep(delayval)
    command_write(var,b'A0X-40Y-120Z180')


def set_reagent(var):
    # command_Write(var,b'A0X-28Y117Z150')

    command_write(var,b'A0X-28Y117Z140')
    time.sleep(delayval2)
    command_write(var,b'd0')
    time.sleep(delayval)
    # command_Write(var,b'A0X-28Y117Z200')
    command_write(var,b'F0');


def put_chip(var):
    command_write(var,b'A0X85Y155Z140')
    time.sleep(1)
    command_write(var,b'e0')
    time.sleep(delayval)


def go_home(var):
    command_write(var,b'A0X0Y0Z140')

    command_write(var,b'h0')

# delayval = 0.6
# delayval2 = 2
#
#
# def get_chip(var):
#     var.write(b'A0X0Y0Z200')
#     time.sleep(delayval)
#     var.write(b'A0X-108Y-46Z200')
#     time.sleep(delayval)
#     var.write(b'A0X-108Y-46Z60')
#     time.sleep(delayval)
#     var.write(b'A0X-108Y-46Z48')
#     time.sleep(delayval)
#     var.write(b'A0X-108Y-46Z200')
#     time.sleep(delayval)
#
#
# def get_reagent(var):
#     var.write(b'A0X-40Y-120Z200')
#     time.sleep(delayval)
#     var.write(b'A0X-40Y-120Z20')
#     time.sleep(delayval)
#     var.write(b'p5')
#     time.sleep(delayval2)
#     var.write(b'A0X-40Y-120Z200')
#     time.sleep(delayval)
#
#
# def set_reagent(var):
#     var.write(b'A0X-28Y117Z200')
#     time.sleep(delayval)
#     var.write(b'A0X-28Y117Z140')
#     time.sleep(delayval)
#     var.write(b'd')
#     time.sleep(delayval2)
#     var.write(b'A0X-28Y117Z200')
#     time.sleep(delayval)
#
#
# def put_chip(var):
#     var.write(b'A0X85Y155Z200')
#     time.sleep(delayval)
#     var.write(b'e')
#     time.sleep(delayval)
#
#
# def go_home(var):
#     var.write(b'A0X0Y0Z200')
#     time.sleep(delayval)
#     var.write(b'h')

