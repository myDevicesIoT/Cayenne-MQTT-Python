#!/usr/bin/env python
import cayenne.client

# Cayenne authentication info. This should be obtained from the Cayenne Dashboard.
MQTT_USERNAME  = "MQTT_USERNAME"
MQTT_PASSWORD  = "MQTT_PASSWORD"
MQTT_CLIENT_ID = "MQTT_CLIENT_ID"


# The callback for when a message is received from Cayenne.
def on_message(message):
    print("message received: " + str(message))
    # If there is an error processing the message return an error string, otherwise return nothing.

client = cayenne.client.CayenneMQTTClient()
client.on_message = on_message
client.begin(MQTT_USERNAME, MQTT_PASSWORD, MQTT_CLIENT_ID)
client.loop_forever()

