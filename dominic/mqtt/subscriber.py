import paho.mqtt.client as mqtt
import threading,time

json_data = {
    "nodeName": "01",
    "block_1": {
        "esp11": {
            "topic": "01/1/esp11",
            "status": 0,
            "SoilMoistureSensor": {"value": 0}
        },
        "esp12": {
            "topic": "01/1/esp12",
            "status": 0,
            "SoilMoistureSensor": {"value": 0}
        }
    },
    "block_2": {
        "esp21": {
            "topic": "01/2/esp21",
            "status": 0,
            "SoilMoistureSensor": {"value": 0}
        },
        "esp22": {
            "topic": "01/2/esp22",
            "status": 0,
            "SoilMoistureSensor": {"value": 0}
        }
    },
    "block_3": {
        "esp31": {
            "topic": "01/3/esp31",
            "status": 0,
            "SoilMoistureSensor": {"value": 0}
        },
        "esp32": {
            "topic": "01/3/esp32",
            "status": 0,
            "SoilMoistureSensor": {"value": 0}
        }
    },
    "block_4": {
        "esp41": {
            "topic": "01/4/esp41",
            "status": 0,
            "SoilMoistureSensor": {"value": 0},
            "AirSensor": {
                "PM10": 0,
                "PM25": 0,
                "PM100": 0,
                "P03": 0,
                "P05": 0,
                "P10": 0,
                "P25": 0,
                "temperature":0,
                "humidity":0
            },
            "TemperatureSensor": {"temperatureC": 0, "temperatureF": 0}
        },
        "esp42": {
            "topic": "01/4/esp42",
            "status": 0,
            "SoilMoistureSensor": {"value": 0}
        }
    }
}
# node-1
# block-1
# esp11
def debug_use():
    json_data['block_1']['esp11']['status'] = 0
    json_data['block_1']['esp12']['status'] = 0
    json_data['block_2']['esp21']['status'] = 0
    json_data['block_2']['esp22']['status'] = 0
    json_data['block_3']['esp31']['status'] = 0
    json_data['block_3']['esp32']['status'] = 0
    json_data['block_4']['esp41']['status'] = 0
    json_data['block_4']['esp22']['status'] = 0
    time.sleep(5)
    print(json_data)


# esp11
def on_connect_0(client, userdata, flags, rc):
    # print("Connected with result code "+str(rc))
    client.subscribe("01/1/esp11")
def on_message_0(client, userdata, msg):
    json_data['block_1']['esp11']['status'] = 1
    if msg.payload.decode()[0:1] == "d":
        json_data['block_1']['esp11']['SoilMoistureSensor']['value']=msg.payload.decode()[2:]
# esp12
def on_connect_1(client, userdata, flags, rc):
    # print("Connected with result code "+str(rc))
    client.subscribe("01/1/esp12")
def on_message_1(client, userdata, msg):
    json_data['block_1']['esp12']['status'] = 1
    if msg.payload.decode()[0:1] == "d":
        json_data['block_1']['esp12']['SoilMoistureSensor']['value']=msg.payload.decode()[2:]

# esp21
def on_connect_2(client, userdata, flags, rc):
    # print("Connected with result code "+str(rc))
    client.subscribe("01/2/esp21")
def on_message_2(client, userdata, msg):
    json_data['block_2']['esp21']['status'] = 1
    if msg.payload.decode()[0:1] == "d":
        json_data['block_2']['esp21']['SoilMoistureSensor']['value']=msg.payload.decode()[2:]

# esp22
def on_connect_3(client, userdata, flags, rc):
    # print("Connected with result code "+str(rc))
    client.subscribe("01/2/esp22")
def on_message_3(client, userdata, msg):
    json_data['block_2']['esp22']['status'] = 1
    if msg.payload.decode()[0:1] == "d":
        json_data['block_2']['esp22']['SoilMoistureSensor']['value']=msg.payload.decode()[2:]

# esp31
def on_connect_4(client, userdata, flags, rc):
    # print("Connected with result code "+str(rc))
    client.subscribe("01/3/esp31")
def on_message_4(client, userdata, msg):
    json_data['block_3']['esp31']['status'] = 1
    if msg.payload.decode()[0:1] == "d":
        json_data['block_3']['esp31']['SoilMoistureSensor']['value']=msg.payload.decode()[2:]

# esp32
def on_connect_5(client, userdata, flags, rc):
    # print("Connected with result code "+str(rc))
    client.subscribe("01/3/esp32")
def on_message_5(client, userdata, msg):
    json_data['block_3']['esp32']['status'] = 1
    if msg.payload.decode()[0:1] == "d":
        json_data['block_3']['esp32']['SoilMoistureSensor']['value']=msg.payload.decode()[2:]

# esp41
def on_connect_6(client, userdata, flags, rc):
    # print("Connected with result code "+str(rc))
    client.subscribe("01/4/esp41")
def on_message_6(client, userdata, msg):
    json_data['block_4']['esp41']['status'] = 1
    if msg.payload.decode()[0:1] == "d":
        json_data['block_4']['esp41']['SoilMoistureSensor']['value']=msg.payload.decode()[2:]

# esp42
def on_connect_7(client, userdata, flags, rc):
    # print("Connected with result code "+str(rc))
    client.subscribe("01/4/esp42")
def on_message_7(client, userdata, msg):
    json_data['block_4']['esp42']['status'] = 1
    if msg.payload.decode()[0:1] == "d":
        json_data['block_4']['esp42']['SoilMoistureSensor']['value']=msg.payload.decode()[2:]

    if msg.payload.decode()[0:4] == "dSTC":
        json_data['block_4']['esp42']['TemperatureSensor']['temperatureC']=msg.payload.decode()[5:]

    if msg.payload.decode()[0:4] == "dSTF":
        json_data['block_4']['esp42']['TemperatureSensor']['temperatureF']=msg.payload.decode()[5:]
    
    if msg.payload.decode()[0:6] == "dAPM10":
        json_data['block_4']['esp42']["AirSensor"]['PM10']=msg.payload.decode()[7:]
    
    if msg.payload.decode()[0:6] == "dAPM25":
        json_data['block_4']['esp42']["AirSensor"]['PM25']=msg.payload.decode()[7:]
    
    if msg.payload.decode()[0:7] == "dAPM100":
        json_data['block_4']['esp42']["AirSensor"]['PM100']=msg.payload.decode()[8:]
    
    if msg.payload.decode()[0:5] == "dAP03":
        json_data['block_4']['esp42']["AirSensor"]['P03']=msg.payload.decode()[6:]
    
    if msg.payload.decode()[0:5] == "dAP05":
        json_data['block_4']['esp42']["AirSensor"]['P05']=msg.payload.decode()[6:]

    if msg.payload.decode()[0:5] == "dAP10":
        json_data['block_4']['esp42']["AirSensor"]['P10']=msg.payload.decode()[6:]

    if msg.payload.decode()[0:5] == "dAP25":
        json_data['block_4']['esp42']["AirSensor"]['P25']=msg.payload.decode()[6:]

    if msg.payload.decode()[0:5] == "dAH":
        json_data['block_4']['esp42']["AirSensor"]['humidity']=msg.payload.decode()[6:]

    if msg.payload.decode()[0:5] == "dAT":
        json_data['block_4']['esp42']["AirSensor"]['temperature']=msg.payload.decode()[6:]

        
        
              


client2 = mqtt.Client()
for i in range(8):
    exec(f'client{i} = mqtt.Client()')
    exec(f"client{i}.connect('10.42.0.1', 1883, 60)")
    exec(f"client{i}.on_connect = on_connect_{i}")
    exec(f"client{i}.on_message = on_message_{i}")
    exec(f'client{i}.loop_start()')
    

t1=threading.Thread(target=debug_use,daemon=True)
while(True):
    x = input('>>')
    if(x == 'exit'):
        break
