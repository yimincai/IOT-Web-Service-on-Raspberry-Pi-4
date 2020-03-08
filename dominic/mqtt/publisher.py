import paho.mqtt.client as mqtt

client=mqtt.Client('Server')
client.connect('localhost',1883,60)
client.publish('topic/test','Hello world!')
client.disconnect()