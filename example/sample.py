import sixfab_iotshield as iotshield



print 'Lux value %d', iotshield.lux()


iotshield.optoRead(opto=1)

for i in range(4):
    print "adc[i]: %d ", iotshield.adc(i)

#contains error sa

iotshield.relay(relayNumber=1,switchStatus=true)



