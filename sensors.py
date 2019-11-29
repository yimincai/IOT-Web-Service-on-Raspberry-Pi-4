import os
import glob
import time
import RPi.GPIO as GPIO
import board
import busio
import serial

# Temperature
base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

def read_device_file():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines

def parse_temperature():
    lines = read_device_file()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.1)
        lines = read_device_file()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temperature_string = lines[1][equals_pos+2:]
        temperature_c = float(temperature_string) / 1000.0
        temperature_f = temperature_c * 9.0 / 5.0 + 32.0
        return temperature_c, temperature_f

# soil
channel = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)
waterStatus = "Water not Detected"
 
def callback(channel):
        if GPIO.input(channel):
            waterStatus = "Water Detected"
        else:
            waterStatus = "Water not Detected"

GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)  # let us know when the pin goes HIGH or LOW
                
# PMS5003

try:
    import struct
except ImportError:
    import ustruct as struct

# For use with Raspberry Pi/Linux:
uart = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=0.25)

def defindData():
    buffer = []
    data = uart.read(32)  # read up to 32 bytes
    data = list(data)
    # print("read: ", data)          # this is a bytearray type

    buffer += data

    while buffer and buffer[0] != 0x42:
        buffer.pop(0)
    dust=None
    for i in range(1):
        if len(buffer) > 200:
            buffer = []  # avoid an overrun if all bad data

        if len(buffer) < 32:
            continue

        if buffer[1] != 0x4d:
            buffer.pop(0)
            continue

        frame_len = struct.unpack(">H", bytes(buffer[2:4]))[0]
        if frame_len != 28:
            buffer = []
            continue

        frame = struct.unpack(">HHHHHHHHHHHHHH", bytes(buffer[4:]))

        pm10_standard, pm25_standard, pm100_standard, pm10_env, \
            pm25_env, pm100_env, particles_03um, particles_05um, particles_10um, \
            particles_25um, particles_50um, particles_100um, skip, checksum = frame

        check = sum(buffer[0:30])

        if check != checksum:
            buffer = []
            continue

        dust={
        'PM 1.0':pm10_standard,
        'PM 2.5':pm25_standard,
        'PM 10':pm100_standard,
        "Particles > 0.3um / 0.1L air:": particles_03um,
        "Particles > 0.5um / 0.1L air:": particles_05um,
        "Particles > 1.0um / 0.1L air:": particles_10um,
        "Particles > 2.5um / 0.1L air:": particles_25um
        }
    
    buffer = buffer[32:]
    
    # Temperature
    c, f = parse_temperature()

    airtemperature={
    "temperatureC": c,
    "temperatureF": f
  }
    # soil
    GPIO.add_event_callback(channel, callback)  # assign function to GPIO PIN, Run function on change

    return {
        "id": "node-01",
        "status": "active",
        "DustSensor":dust,
        "AirTemperature": airtemperature,
        "SoilMoistureSensor": waterStatus
        }

print(defindData())