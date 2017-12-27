#import libraries
from enum import Enum
from .ADS1x15 import ADS1015
import time
import RPi.GPIO as GPIO
import serial


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
##-----setting pin------
statusPin = 13
power_key = 12

port = "/dev/ttyS0"

GPIO.setup(statusPin, GPIO.IN)
GPIO.setup(power_key, GPIO.OUT)

class switchStatus(Enum):
    OFF = False
    ON = True

class relayNumber(Enum):
    relay1 = 21
    relay2 = 26

class opto(Enum):
    opto1 = 20
    opto2 = 19



def lux():
    adc = ADS1015(address=0x49, busnum=1)
    rawLux=adc.read_adc(2,gain=1)
    lux = rawLux*100/1580
    return lux

def relay(relayNumber,switchStatus):
    GPIO.setup(relayNumber, GPIO.OUT)
    GPIO.output(relayNumber, switchStatus)
    #print "RELAY1: ON"
    time.sleep(1)


def status():
    def turnModuleOn():
        GPIO.output(power_key, 1)
        time.sleep(2)
        GPIO.output(power_key, 0)
        time.sleep(2)

    def checkStatus():
        status = GPIO.input(statusPin)
        if status == 0:
            print "Module turned OFF"
        else:
            print "Module turned ON"
        time.sleep(0.1)
        return status

    status = checkStatus()

    if status == 0:
        turnModuleOn()

'''
def connectivity(string):
    ser = serial.Serial(port, baudrate=115200, timeout=0.5)

    ser.write(string+'\r')
    #ser.write('AT\r')
    ser.readline()
    return ser.readline()
    time.sleep(1)
'''

def adc(i):
    adc = ADS1015(address=0x49, busnum=1)
    adcValues = [0] * 4
    adcValues[i] = adc.read_adc(i, gain=1)
    return adcValues[i]



def optoRead(opto):
    GPIO.setup(opto, GPIO.IN)
    optoReading = GPIO.input(opto)
    if (optoReading==optoRead.HIGH):
        return "LOW"
    elif():
        print "HIGH"
