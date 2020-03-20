import paho.mqtt.client as mqtt

# This is the Subscriber
# command=['data']
# do=[]
# def data(client,msg):
#   client.publish(msg.topic,)

def on_connect(client, userdata, flags, rc):
  # print("Connected with result code "+str(rc))
  client.subscribe("hahaha")

def on_message(client, userdata, msg):
  print(msg.payload.decode())
  # if msg.payload.decode() == "Hello world!":
  #   print("Yes!")
  #   client.disconnect()

def on_connect_2(client, userdata, flags, rc):
  # print("Connected with result code "+str(rc))
  client.subscribe("hehehe")
    
client = mqtt.Client()
client.connect('localhost',1883,60)

client.on_connect = on_connect
client.on_message = on_message

client2 = mqtt.Client()
client2.connect('localhost',1883,60)

client2.on_connect = on_connect_2
client2.on_message = on_message


client.loop_start()
client2.loop_start()

while(True):
  x=input('>>')
  if(x=='exit'):
    break