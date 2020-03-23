import paho.mqtt.client as mqtt
import threading,time,json
# import requests
url=''


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
    while True:
        # every 5 sec set status back to 0
        json_data['block_1']['esp11']['status'] = 0
        json_data['block_1']['esp12']['status'] = 0
        json_data['block_2']['esp21']['status'] = 0
        json_data['block_2']['esp22']['status'] = 0
        json_data['block_3']['esp31']['status'] = 0
        json_data['block_3']['esp32']['status'] = 0
        json_data['block_4']['esp41']['status'] = 0
        json_data['block_4']['esp42']['status'] = 0
        # change to request to django by url 
        ###########################################
        # while(True):
        #     r=requests.get(url,params=json_data)
        #     if(r.json()=='data recv'):
        #         break
        ###########################################
        print(json.dumps(json_data,indent=4))
        time.sleep(5)


# esp11
def on_connect_0(client, userdata, flags, rc):
    # print("Connected with result code "+str(rc))
    client.subscribe("01/1/esp11")
def on_message_0(client, userdata, msg):
    json_data['block_1']['esp11']['status'] = 1
    x=msg.payload.decode().split()
    if x[0] == "d":
        json_data['block_1']['esp11']['SoilMoistureSensor']['value']=x[1]
# esp12
def on_connect_1(client, userdata, flags, rc):
    # print("Connected with result code "+str(rc))
    client.subscribe("01/1/esp12")
def on_message_1(client, userdata, msg):
    json_data['block_1']['esp12']['status'] = 1
    x=msg.payload.decode().split()
    if x[0] == "d":
        json_data['block_1']['esp12']['SoilMoistureSensor']['value']=x[1]

# esp21
def on_connect_2(client, userdata, flags, rc):
    # print("Connected with result code "+str(rc))
    client.subscribe("01/2/esp21")
def on_message_2(client, userdata, msg):
    json_data['block_2']['esp21']['status'] = 1
    x=msg.payload.decode().split()
    if x[0] == "d":
        json_data['block_2']['esp21']['SoilMoistureSensor']['value']=x[1]

# esp22
def on_connect_3(client, userdata, flags, rc):
    # print("Connected with result code "+str(rc))
    client.subscribe("01/2/esp22")
def on_message_3(client, userdata, msg):
    json_data['block_2']['esp22']['status'] = 1
    x=msg.payload.decode().split()
    if x[0] == "d":
        json_data['block_2']['esp22']['SoilMoistureSensor']['value']=x[1]

# esp31
def on_connect_4(client, userdata, flags, rc):
    # print("Connected with result code "+str(rc))
    client.subscribe("01/3/esp31")
def on_message_4(client, userdata, msg):
    json_data['block_3']['esp31']['status'] = 1
    x=msg.payload.decode().split()
    if x[0] == "d":
        json_data['block_3']['esp31']['SoilMoistureSensor']['value']=x[1]

# esp32
def on_connect_5(client, userdata, flags, rc):
    # print("Connected with result code "+str(rc))
    client.subscribe("01/3/esp32")
def on_message_5(client, userdata, msg):
    json_data['block_3']['esp32']['status'] = 1
    x=msg.payload.decode().split()
    if x[0] == "d":
        json_data['block_3']['esp32']['SoilMoistureSensor']['value']=x[1]

# esp41
def on_connect_6(client, userdata, flags, rc):
    # print("Connected with result code "+str(rc))
    client.subscribe("01/4/esp41")
def on_message_6(client, userdata, msg):
    # print(msg.payload.decode())
    json_data['block_4']['esp41']['status'] = 1
    x=msg.payload.decode().split()
    if x[0] == "d":
        json_data['block_4']['esp41']['SoilMoistureSensor']['value']=x[1]

    x=msg.payload.decode().split()
    if x[0] == "dSTC":
        json_data['block_4']['esp41']['TemperatureSensor']['temperatureC']=x[1]

    x=msg.payload.decode().split()
    if x[0] == "dSTF":
        json_data['block_4']['esp41']['TemperatureSensor']['temperatureF']=x[1]
    
    x=msg.payload.decode().split()
    if x[0] == "dAPM10":
        json_data['block_4']['esp41']["AirSensor"]['PM10']=x[1]
    
    x=msg.payload.decode().split()
    if x[0] == "dAPM25":
        json_data['block_4']['esp41']["AirSensor"]['PM25']=x[1]
    
    x=msg.payload.decode().split()
    if x[0] == "dAPM100":
        json_data['block_4']['esp41']["AirSensor"]['PM100']=x[1]
    
    x=msg.payload.decode().split()
    if x[0] == "dAP03":
        json_data['block_4']['esp41']["AirSensor"]['P03']=x[1]
    
    x=msg.payload.decode().split()
    if x[0] == "dAP05":
        json_data['block_4']['esp41']["AirSensor"]['P05']=x[1]

    x=msg.payload.decode().split()
    if x[0] == "dAP10":
        json_data['block_4']['esp41']["AirSensor"]['P10']=x[1]

    x=msg.payload.decode().split()
    if x[0] == "dAP25":
        json_data['block_4']['esp41']["AirSensor"]['P25']=x[1]

    x=msg.payload.decode().split()
    if x[0] == "dAH":
        json_data['block_4']['esp41']["AirSensor"]['humidity']=x[1]

    x=msg.payload.decode().split()
    if x[0] == "dAT":
        json_data['block_4']['esp41']["AirSensor"]['temperature']=x[1]

        
        
# esp42
def on_connect_7(client, userdata, flags, rc):
    # print("Connected with result code "+str(rc))
    client.subscribe("01/4/esp42")
def on_message_7(client, userdata, msg):
    json_data['block_4']['esp42']['status'] = 1
    x=msg.payload.decode().split()
    if x[0] == "d":
        json_data['block_4']['esp42']['SoilMoistureSensor']['value']=x[1]
              


client2 = mqtt.Client()
for i in range(8):
    
    exec('client'+str(i)+' = mqtt.Client()')
    exec("client"+str(i)+".connect('localhost', 1883, 60)")
    exec("client"+str(i)+".on_connect = on_connect_"+str(i))
    exec("client"+str(i)+".on_message = on_message_"+str(i))
    exec("client"+str(i)+".loop_start()")
    
# thread for keep print json data
t1=threading.Thread(target=debug_use,daemon=True)
t1.start()
while(True):
    x = input('>>')
    if(x == 'exit'):
        break
