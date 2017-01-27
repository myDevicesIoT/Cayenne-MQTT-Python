#!/usr/bin/env python
import cayenne.client
import time
import argparse
import sys
import traceback


parser = argparse.ArgumentParser(description='Cayenne MQTT Test.')
parser.add_argument('--host', help='hostname', default='mqtt.mydevices.com')
parser.add_argument('--port', help='port', default=1883)
parser.add_argument('--username', help='username', default='username')
parser.add_argument('--password', help='password', default='password')
parser.add_argument('--clientID', help='clientID', default='clientID')

args = parser.parse_args()
print(args)

try:
    done = False
    # The callback for when a message is received from Cayenne.
    def on_message(message):
        if message.msg_id == "senderror":
            # Test sending an error string.
            return "error response"
        if message.msg_id == "done":
            #The "done" message should be the last message so we set the done flag
            global done
            done = True

    client = cayenne.client.CayenneMQTTClient()
    client.on_message = on_message
    client.begin(args.username, args.password, args.clientID, args.host, args.port)
    start = time.time()
    while not client.connected:
        client.loop()

    print("Test publishing data")
    client.virtualWrite(0, 0)
    client.celsiusWrite(1, 1)
    client.fahrenheitWrite(2, 2)
    client.kelvinWrite(3, 3)
    client.luxWrite(4, 4)
    client.pascalWrite(5, 5)
    client.hectoPascalWrite(6, 6)
    client.accelWrite(7, 7.01, 7.02, -7.03)
    client.gpsWrite(8, 27.986065, 86.922623, 29029)

    print("Test receiving commands")
    client.mqttPublish(client.rootTopic + '/cmd/10', 'senderror,0')
    client.mqttPublish(client.rootTopic + '/cmd/11', 'sendok,1')
    client.mqttPublish(client.rootTopic + '/cmd/12', 'done,1')
    
    start = time.time()
    while True:
        loop_start = time.time()
        client.loop()
        if done and (time.time() - loop_start >= 1):
            break
        if (time.time() - start >= 10):
            raise Exception("Timed out while waiting for commands")
        
except:
    print(str(traceback.format_exc()))
    print('Tests failed with exception.')
    sys.exit(1)

print('Tests finished without errors')    
sys.exit(0)

