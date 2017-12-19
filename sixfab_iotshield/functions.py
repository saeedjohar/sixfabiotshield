from .ADS1x15 import ADS1015
import time
import RPi.GPIO as GPIO
import serial

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
##-----setting pin------
statusPin = 13
power_key = 12
relay1 = 21
relay2 = 26
opto1 = 20
opto2 = 19
adc=ADS1015(address=0x49, busnum=1)



def lux():
    #print'This is lux'

    rawLux=adc.read_adc(2,gain=1)
    lux = rawLux*100/1580
    print 'Lux : %d' %lux


def relay():
    GPIO.setup(relay1, GPIO.OUT)
    GPIO.setup(relay2, GPIO.OUT)

    print "----------RELAY TEST----------"

    GPIO.output(relay1, True)
    print "RELAY1: ON"
    time.sleep(1)

    GPIO.output(relay1, False)
    print "RELAY1: OFF"
    time.sleep(2);

    GPIO.output(relay2, True)
    print "RELAY2: ON"
    time.sleep(1)

    GPIO.output(relay2, False)
    print "RELAY2: OFF"
    time.sleep(2)

def status():
    GPIO.setup(statusPin, GPIO.IN)
    GPIO.setup(power_key, GPIO.OUT)

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

def connectivity():
    port = "/dev/ttyS0"
    ser = serial.Serial(port, baudrate=115200, timeout=0.5)

    print "---------Checking SIM and Connection---------"
    # time.sleep(0.5)
    ser.write('AT\r')
    print ser.readline()
    print ser.readline()
    time.sleep(1)
    ser.write('AT+CPIN?\r')
    print ser.readline()
    print ser.readline()
    ser.close()
    time.sleep(0.1)

def adc(i):
    #print "----------Printing ADS1015 values----------"
    adcValues = [0] * 4

    #for i in range(0, 4):
    #   adcValues[i] = adc.read_adc(i, gain=1)
    #   print "ADC Ch%d : %d" % (i, adcValues[i])

    adcValues[i] = adc.read_adc(i, gain=1)

def opto():
    GPIO.setup(opto1, GPIO.IN)
    GPIO.setup(opto2, GPIO.IN)
    print "----------OPTO TEST----------"

    readOpto1 = GPIO.input(opto1)
    readOpto2 = GPIO.input(opto2)
    if (readOpto1 == 1):
        print "INPUT1: LOW"
    else:
        print "INPUT1: HIGH"

    if (readOpto2 == 1):
        print "INPUT2: LOW"
    else:
        print "INPUT2: HIGH"
