Cayenne MQTT Python Library
***************************
The Cayenne MQTT Python Library provides functions to easily connect to the `Cayenne IoT project builder <https://mydevices.com>`_. With it you can send data to and receive data from Cayenne.

Requirements
============
* `Python 2.7.9+ or 3.4+ <https://www.python.org/downloads/>`_.
* `This library <https://github.com/myDevicesIoT/Cayenne-MQTT-Python/archive/master.zip>`_.
* `Eclipse Paho MQTT Python client library <https://github.com/eclipse/paho.mqtt.python>`_. This is installed as part of the Cayenne library installation.

Getting Started
===============
Installation
------------
This library can be installed using pip:
::

  pip install cayenne-mqtt

It can also be installed from the repository:
::

  git clone https://github.com/myDevicesIoT/Cayenne-MQTT-Python
  cd Cayenne-MQTT-Python
  python setup.py install
  
Cayenne Setup
-------------
1. Create your Cayenne account at https://mydevices.com.
2. Add a new device using the Bring Your Own Thing API selection.

Examples
--------
Simple examples are available in the repository here: https://github.com/myDevicesIoT/Cayenne-MQTT-Python/tree/master/examples.

Below is an example of a simple client that publishes some sample data and receives data from Cayenne in a message callback. The Cayenne authentication variables must be modified with the authentication info you received when adding a new device in Cayenne:
::

  import cayenne.client
  import time

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
  # For a secure connection use port 8883 when calling client.begin:
  # client.begin(MQTT_USERNAME, MQTT_PASSWORD, MQTT_CLIENT_ID, port=8883)

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

Documentation
-------------
For more detailed info about the Cayenne client API you can use **pydoc**.
::

  pydoc cayenne.client
  

Additional Cayenne MQTT Libraries
=================================
Additional libraries are available for connecting to Cayenne with other languages. These can be found at https://github.com/myDevicesIoT.
