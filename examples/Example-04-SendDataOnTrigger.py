#!/usr/bin/env python
import cayenne.client
import time
import logging

# Cayenne authentication info. This should be obtained from the Cayenne Dashboard.
MQTT_USERNAME  = "MQTT_USERNAME"
MQTT_PASSWORD  = "MQTT_PASSWORD"
MQTT_CLIENT_ID = "MQTT_CLIENT_ID"

TRIGGER_CHANNEL = 2  #Virtual channel for publishing the trigger value.
DATA_CHANNEL = 1     #Virtual channel for publishing the sensor data.
THRESHOLD = 6        #Threshold for the trigger.

i=0
timestamp = 0
send_below_threshold = False #Set to true if the trigger should happen when the data value is below the threshold, 
                             #false if it should happen when the data value is above or equal to the threshold.
crossed_threshold = False

# The callback for when a message is received from Cayenne.
def on_message(message):    
    print("message received: " + str(message))
    # If there is an error processing the message return an error string, otherwise return nothing.

client = cayenne.client.CayenneMQTTClient()
client.on_message = on_message
client.begin(MQTT_USERNAME, MQTT_PASSWORD, MQTT_CLIENT_ID, loglevel=logging.INFO)
# For a secure connection use port 8883 when calling client.begin:
# client.begin(MQTT_USERNAME, MQTT_PASSWORD, MQTT_CLIENT_ID, port=8883, loglevel=logging.INFO)

def send_trigger_value(trigger_channel, sensor_value, threshold, send_below_threshold):
    global crossed_threshold
    if (((sensor_value >= threshold) and not send_below_threshold) or ((sensor_value < threshold) and send_below_threshold)):
        if not crossed_threshold:
            client.virtualWrite(trigger_channel, 1, "digital_sensor", "d")
            crossed_threshold = True
    else:
        client.virtualWrite(trigger_channel, 0, "digital_sensor", "d")
        crossed_threshold = False


while True:
    client.loop()
    if (time.time() > timestamp + 10):
        sensor_value =  i 
        client.celsiusWrite(DATA_CHANNEL, sensor_value)
        send_trigger_value(TRIGGER_CHANNEL, sensor_value, THRESHOLD, send_below_threshold)
        timestamp = time.time()
        i = i + 1
        if (i == 12): # Reset the sensor value to test that the trigger gets reset.
            i = 0
