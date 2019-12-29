import paho.mqtt.client as mqtt
import datetime

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    # client.subscribe("$SYS/#")
    client.subscribe(topic)
    client.subscribe(topic+"/#")

def on_subscribe(client, userdata, mid, granted_qos, *args, **kwargs):
	print(str(mid))

def on_log(client, userdata, level, buf):
	print("log: ",buf)

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
	timestamp=str(datetime.datetime.now())
	print(timestamp + ": " + msg.topic+" ("+str(msg.mid)+") "+str(msg.payload)+" "+str(msg.dup)+" "+str(msg.qos)+" - "+str(msg.info))


clientid="123888932589762459/#"
clientid="123888932589762459/+"
# clientid="123888932589762459"

topic="HV19/gifts/123888932589762459"

client = mqtt.Client(client_id=clientid, clean_session=True, transport='websockets')
client.on_connect = on_connect
client.on_subscribe = on_subscribe
client.on_message = on_message
client.on_log = on_log

client.username_pw_set('workshop', '2fXc7AWINBXyruvKLiX')
client.connect("whale.hacking-lab.com", 9001, 60)

print("Looping")
client.loop_forever()
