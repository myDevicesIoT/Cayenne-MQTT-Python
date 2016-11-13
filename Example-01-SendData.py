#!/usr/bin/env python
import Cayenne
import time

MQTT_USERNAME  = "4af7bb30-a878-11e6-a85d-c165103f15c2"
MQTT_PASSWORD  = "00612fd8d84aff146beb773f6b118a5517115b27"
MQTT_CLIENT_ID = "0dd6bf00-a87b-11e6-a7c1-b395fc8a1540"


client = Cayenne.CayenneMQTTClient()

client.begin(MQTT_USERNAME, MQTT_PASSWORD, MQTT_CLIENT_ID)

i=0
timestamp = 0

while True:
    client.loop()
    
    if (time.time() > timestamp + 10):
        client.celsiusWrite(1, i)
        client.luxWrite(2, i*10)
        client.hectoPascalWrite(3, i+800)
        timestamp = time.time()
        i = i+1
