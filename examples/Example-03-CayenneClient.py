#!/usr/bin/env python
from cayenne import client, datatypes
import time

# Cayenne authentication info. This should be obtained from the Cayenne Dashboard.
MQTT_USERNAME  = "MQTT_USERNAME"
MQTT_PASSWORD  = "MQTT_PASSWORD"
MQTT_CLIENT_ID = "MQTT_CLIENT_ID"


# The callback for when a message is received from Cayenne.
def on_message(message):
    print("message received: " + str(message))
    # If there is an error processing the message return an error string, otherwise return nothing.
    
cayenne_client = client.CayenneMQTTClient()
cayenne_client.on_message = on_message
cayenne_client.begin(MQTT_USERNAME, MQTT_PASSWORD, MQTT_CLIENT_ID)

i=0
timestamp = 0

while True:
    cayenne_client.loop()
    
    if (time.time() > timestamp + 10):
        cayenne_client.celsiusWrite(1, i)
        cayenne_client.luxWrite(2, i*10)
        cayenne_client.hectoPascalWrite(3, i+800)
        cayenne_client.virtualWrite(4, i%2, datatypes.TYPE_DIGITAL_SENSOR, datatypes.UNIT_DIGITAL)
        timestamp = time.time()
        i = i+1
