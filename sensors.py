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
#GPIO SETUP
channel = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)
 
def callback(channel):
        if GPIO.input(channel):
                print("---------------------------------------")
                print("Water Detected!")
                print("---------------------------------------")
        else:
                print("---------------------------------------")
                print("Water not Detected!")
                print("---------------------------------------")

GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)  # let us know when the pin goes HIGH or LOW
                
# PMS5003

try:
    import struct
except ImportError:
    import ustruct as struct

# Connect the sensor TX pin to the board/computer RX pin
# For use with a microcontroller board:

#uart = busio.UART(board.TX, board.RX, baudrate=9600)

# For use with Raspberry Pi/Linux:
uart = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=0.25)

# For use with USB-to-serial cable:
# import serial
# uart = serial.Serial("/dev/ttyUSB0", baudrate=9600, timeout=0.25)

buffer = []

while True:
    data = uart.read(32)  # read up to 32 bytes
    data = list(data)
    # print("read: ", data)          # this is a bytearray type

    buffer += data

    while buffer and buffer[0] != 0x42:
        buffer.pop(0)

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

    # PMS5003
    if check != checksum:
        buffer = []
        continue
    print("Concentration Units (standard)")
    print("---------------------------------------")
    print("PM 1.0: %d\tPM2.5: %d\tPM10: %d" %
              (pm10_standard, pm25_standard, pm100_standard))
    print("Concentration Units (environmental)")
    print("---------------------------------------")
    print("PM 1.0: %d\tPM2.5: %d\tPM10: %d" % (pm10_env, pm25_env, pm100_env))
    print("---------------------------------------")
    print("Particles > 0.3um / 0.1L air:", particles_03um)
    print("Particles > 0.5um / 0.1L air:", particles_05um)
    print("Particles > 1.0um / 0.1L air:", particles_10um)
    print("Particles > 2.5um / 0.1L air:", particles_25um)
    
    buffer = buffer[32:]
    
    # Temperature
    c, f = parse_temperature()
    print("---------------------------------------")
    print('溫度為攝氏 {:.2f} 度，華氏 {:.2f} 度'.format(c, f))
    print("---------------------------------------")
        
    # soil
    GPIO.add_event_callback(channel, callback)  # assign function to GPIO PIN, Run function on change
    time.sleep(1)
# Concentration Units (standard)
# ---------------------------------------
# PM 1.0: 2   PM2.5: 3    PM10: 4
# Concentration Units (environmental)
# ---------------------------------------
# PM 1.0: 2   PM2.5: 3    PM10: 4
# ---------------------------------------
# Particles > 0.3um / 0.1L air: 468
# Particles > 0.5um / 0.1L air: 141
# Particles > 1.0um / 0.1L air: 18
# Particles > 2.5um / 0.1L air: 3
# ---------------------------------------
# 溫度為攝氏 28.69 度，華氏 83.64 度
# ---------------------------------------
# Water Detected!
# ---------------------------------------
# Water not Detected!
# ---------------------------------------