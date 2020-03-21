import paho.mqtt.client as mqtt

client=mqtt.Client('Server')
client.connect('localhost',1883,60)
client.publish('hahaha','Hello world!')
client.disconnect()

client=mqtt.Client('Server')
client.connect('localhost',1883,60)
client.publish('hehehe','Hello world!')
client.disconnect()