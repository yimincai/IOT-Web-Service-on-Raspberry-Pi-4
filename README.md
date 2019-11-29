# IOT Web Service on Raspberry Pi 4

## Abstract

This project will used flask to return the sensors data to "http://yourip/node-01" as a web service in JSON type.

## Requirement

### Devices
- [Raspberry Pi 4](https://www.raspberrypi.com.tw/28040/raspberry-pi-4-model-b/)
- [PMS5003T](https://www.taiwaniot.com.tw/product/pms5003t-g5t-%E6%94%80%E8%97%A4%E7%B2%89%E5%A1%B5%E6%BA%AB%E6%BF%95%E5%BA%A6%E4%BA%8C%E5%90%88%E4%B8%80%E6%84%9F%E6%B8%AC%E5%99%A8/)
- [Soil Moisture Detection](https://www.amazon.com/gp/product/B071F4RDHY/ref=as_li_ss_tl?ie=UTF8&linkCode=sl1&tag=piddlerinther-20&linkId=77f1c0f9c67c51d76b687628afa62ce1&language=en_US)
- [DS18B20](https://www.playrobot.com/temperature-humidity/841-temperature-sensor-waterproof-ds18b20.html)

### Software
- Linux OS
- Python 3
- flask, RPI.GPIO, board, serial, adafruit-blinka

## Usage
- Download and install Python 3 on [Official Website](https://www.python.org/downloads/)
- Install require libs:
```bash
$ pip install flask RPi.GPIO board serial adafruit-blinka
```
- Download the project to /home/pi
- add this line to ```/ect/profile``` to let project auto run on boot
```bash
$ sudo python3 /home/pi/Sensors/app.py &
```
- Change python files permission 
```bash
$ sudo chmod 777 /home/pi/Sensors/app.py 
$ sudo chmod 777 /home/pi/Sensor/sensors.py
```
- Reboot your Raspberry Pi 4 to test the service
```bash
$ sudo reboot
```