from .ADS1x15 import ADS1015
def lux():
    print'This is lux'
    adc=ADS1015(address=0x49, busnum=1)
    rawLux=adc.read_adc(2,gain=1)
    lux = rawLux*100/1580
    print 'Lux : %d' %lux
