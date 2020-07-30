import threading
import paho.mqtt.client as mqtt
import time
import json
import requests
url = 'http://localhost:8080/recv_data'


json_data = {
    "nodeName": "01",
    "esp11": {
        "topic": "01/1/esp11",
        "status": 0,
        "SoilMoistureSensor": 0
    },
    "esp12": {
        "topic": "01/1/esp12",
        "status": 0,
        "SoilMoistureSensor": 0
    },
    "esp21": {
        "topic": "01/2/esp21",
        "status": 0,
        "SoilMoistureSensor":  0
    },
    "esp22": {
        "topic": "01/2/esp22",
        "status": 0,
        "SoilMoistureSensor":  0
    },
    "esp31": {
        "topic": "01/3/esp31",
        "status": 0,
        "SoilMoistureSensor":  0
    },
    "esp32": {
        "topic": "01/3/esp32",
        "status": 0,
        "SoilMoistureSensor":  0
    },
    "esp41": {
        "topic": "01/4/esp41",
        "status": 0,
        "SoilMoistureSensor": 0,
        "AirSensor": {
            "PM10": 0,
            "PM25": 0,
            "PM100": 0,
            "P03": 0,
            "P05": 0,
            "P10": 0,
            "P25": 0,
            "temperature": 0,
            "humidity": 0
        },
        "TemperatureSensor": {
            "temperatureC": 0, 
            "temperatureF": 0
            },
    },
    "esp42": {
        "topic": "01/4/esp42",
        "status": 0,
        "SoilMoistureSensor": 0
    }
}

# node-1
# block-1
# esp11

def debug_use():
    while True:
        # every 5 sec set status back to 0
        json_data['esp11']['status'] = 0
        json_data['esp12']['status'] = 0
        json_data['esp21']['status'] = 0
        json_data['esp22']['status'] = 0
        json_data['esp31']['status'] = 0
        json_data['esp32']['status'] = 0
        json_data['esp41']['status'] = 0
        json_data['esp42']['status'] = 0
        # change to request to django by url
        ###########################################
        # while(True):
        #     r=requests.get(url,params=json_data)
        #     if(r.json()=='data recv'):
        #         break
        ###########################################
        print(json.dumps(json_data, indent=4))
        time.sleep(5)


# esp11
def on_connect_0(client, userdata, flags, rc):
    # print("Connected with result code "+str(rc))
    client.subscribe("01/1/esp11")
def on_message_0(client, userdata, msg):
    json_data['esp11']['status'] = 1
    x = msg.payload.decode().split()
    if x[0] == "d":
        json_data['esp11']['SoilMoistureSensor'] = x[1]
# esp12
def on_connect_1(client, userdata, flags, rc):
    # print("Connected with result code "+str(rc))
    client.subscribe("01/1/esp12")
def on_message_1(client, userdata, msg):
    json_data['esp12']['status'] = 1
    x = msg.payload.decode().split()
    if x[0] == "d":
        json_data['esp12']['SoilMoistureSensor'] = x[1]

# esp21
def on_connect_2(client, userdata, flags, rc):
    # print("Connected with result code "+str(rc))
    client.subscribe("01/2/esp21")
def on_message_2(client, userdata, msg):
    json_data['esp21']['status'] = 1
    x = msg.payload.decode().split()
    if x[0] == "d":
        json_data['esp21']['SoilMoistureSensor'] = x[1]

# esp22
def on_connect_3(client, userdata, flags, rc):
    # print("Connected with result code "+str(rc))
    client.subscribe("01/2/esp22")
def on_message_3(client, userdata, msg):
    json_data['esp22']['status'] = 1
    x = msg.payload.decode().split()
    if x[0] == "d":
        json_data['esp22']['SoilMoistureSensor'] = x[1]

# esp31
def on_connect_4(client, userdata, flags, rc):
    # print("Connected with result code "+str(rc))
    client.subscribe("01/3/esp31")
def on_message_4(client, userdata, msg):
    json_data['esp31']['status'] = 1
    x = msg.payload.decode().split()
    if x[0] == "d":
        json_data['esp31']['SoilMoistureSensor'] = x[1]

# esp32
def on_connect_5(client, userdata, flags, rc):
    # print("Connected with result code "+str(rc))
    client.subscribe("01/3/esp32")
def on_message_5(client, userdata, msg):
    json_data['esp32']['status'] = 1
    x = msg.payload.decode().split()
    if x[0] == "d":
        json_data['esp32']['SoilMoistureSensor'] = x[1]

# esp41
def on_connect_6(client, userdata, flags, rc):
    # print("Connected with result code "+str(rc))
    client.subscribe("01/4/esp41")
def on_message_6(client, userdata, msg):
    # print(msg.payload.decode())
    json_data['esp41']['status'] = 1
    x = msg.payload.decode().split()
    if x[0] == "d":
        json_data['esp41']['SoilMoistureSensor'] = x[1]

    x = msg.payload.decode().split()
    if x[0] == "dSTC":
        json_data['esp41']['TemperatureSensor']['temperatureC'] = x[1]

    x = msg.payload.decode().split()
    if x[0] == "dSTF":
        json_data['esp41']['TemperatureSensor']['temperatureF'] = x[1]

    x = msg.payload.decode().split()
    if x[0] == "dAPM10":
        json_data['esp41']["AirSensor"]['PM10'] = x[1]

    x = msg.payload.decode().split()
    if x[0] == "dAPM25":
        json_data['esp41']["AirSensor"]['PM25'] = x[1]

    x = msg.payload.decode().split()
    if x[0] == "dAPM100":
        json_data['esp41']["AirSensor"]['PM100'] = x[1]

    x = msg.payload.decode().split()
    if x[0] == "dAP03":
        json_data['esp41']["AirSensor"]['P03'] = x[1]

    x = msg.payload.decode().split()
    if x[0] == "dAP05":
        json_data['esp41']["AirSensor"]['P05'] = x[1]

    x = msg.payload.decode().split()
    if x[0] == "dAP10":
        json_data['esp41']["AirSensor"]['P10'] = x[1]

    x = msg.payload.decode().split()
    if x[0] == "dAP25":
        json_data['esp41']["AirSensor"]['P25'] = x[1]

    x = msg.payload.decode().split()
    if x[0] == "dAH":
        json_data['esp41']["AirSensor"]['humidity'] = x[1]

    x = msg.payload.decode().split()
    if x[0] == "dAT":
        json_data['esp41']["AirSensor"]['temperature'] = x[1]



# esp42
def on_connect_7(client, userdata, flags, rc):
    # print("Connected with result code "+str(rc))
    client.subscribe("01/4/esp42")
def on_message_7(client, userdata, msg):
    json_data['esp42']['status'] = 1
    x = msg.payload.decode().split()
    if x[0] == "d":
        json_data['esp42']['SoilMoistureSensor'] = x[1]


def run_all_mqtt_recv():
    for i in range(8):

        exec('client'+str(i)+" = mqtt.Client()")
        exec("client"+str(i)+".connect('localhost', 1883, 60)")
        exec("client"+str(i)+".on_connect = on_connect_"+str(i))
        exec("client"+str(i)+".on_message = on_message_"+str(i))
        exec("client"+str(i)+".loop_start()")

def run():
    while True:
        try:
            resp=requests.get(url=url,params=json.dumps(json_data))
            # print(resp)
            # print(json.dumps(json_data))
            while resp.status_code!=200:
                requests.get(url=url,params=json.dumps(json_data))
            time.sleep(5)  
        except Exception as e:
            print(e)
            time.sleep(5)  


if __name__ == "__main__":
    run_all_mqtt_recv()
    run()
