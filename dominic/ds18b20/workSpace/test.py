from machine import Pin
import onewire
import ds18x20
import time
 
ow = onewire.OneWire(Pin(21))   #Init wire
ow.scan()
ds=ds18x20.DS18X20(ow)          #create ds18x20 object
while True:
  roms=ds.scan()                #scan ds18x20
  ds.convert_temp()             #convert temperature
  for rom in roms:
    print(ds.read_temp(rom))    #display 
  time.sleep(1)
