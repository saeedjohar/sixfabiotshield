

def lux():
    from .ADS1x15 import ADS1015
    #print'This is lux'
    adc=ADS1015(address=0x49, busnum=1)
    rawLux=adc.read_adc(2,gain=1)
    lux = rawLux*100/1580
    print 'Lux : %d' %lux

def relay():
    import time
    import RPi.GPIO as GPIO
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    relay1 = 21
    relay2 = 26

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