import paho.mqtt.client as mqtt

TYPE_BAROMETRIC_PRESSURE = "bp" # Barometric pressure
TYPE_BATTERY = "batt" # Battery
TYPE_LUMINOSITY = "lum" # Luminosity
TYPE_PROXIMITY = "prox" # Proximity
TYPE_RELATIVE_HUMIDITY = "rel_hum" # Relative Humidity
TYPE_TEMPERATURE = "temp" # Temperature
TYPE_VOLTAGE = "voltage" # Voltage

UNIT_UNDEFINED = "null"
UNIT_PASCAL = "pa" # Pascal
UNIT_HECTOPASCAL = "hpa" # Hectopascal
UNIT_PERCENT = "p" # % (0 to 100)
UNIT_RATIO = "r" # Ratio
UNIT_VOLTS = "v" # Volts
UNIT_LUX = "lux" # Lux
UNIT_CENTIMETER = "cm" # Centimeter
UNIT_METER = "m" # Meter
UNIT_DIGITAL = "d" # Digital (0/1)
UNIT_FAHRENHEIT = "f" # Fahrenheit
UNIT_CELSIUS = "c" # Celsius
UNIT_KELVIN = "k" # Kelvin
UNIT_MILLIVOLTS = "mv" # Millivolts

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, cayenne, rc):
    
    print("Connected with result code "+str(rc))
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    cayenne.setConnected()
    client.subscribe("$SYS/#")

    cayenne.mqttPublish("%s/sys/model" % cayenne.rootTopic, "Python")
    cayenne.mqttPublish("%s/sys/version" % cayenne.rootTopic, "1.0")


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    
    
class CayenneMQTTClient():
    
    client = None
    rootTopic = ""
    connected = False

    def dataTopic(self, channel):
        return "%s/%s" % (rootTopic, channel)
    
    def mqttPublish(self, topic, payload):
        print("PUB %s\n%s\n" % (topic, payload))
        self.client.publish(topic, payload, 0, False)    

    def begin(self, username, password, clientid):
        self.rootTopic = "v1/%s/things/%s" % (username, clientid)
        self.client = mqtt.Client(client_id=clientid, clean_session=True, userdata=self)
        self.client.on_connect = on_connect
        self.client.on_message = on_message
        self.client.username_pw_set(username, password)
        self.client.connect("mqtt.mydevices.com", 1883, 60)
        print("Connecting to mqtt.mydevices.com...")

    def setConnected(self):
        self.connected = True
    
    def loop(self):
        self.client.loop()
    
    def loop_forever(self):
        self.client().loop_forever()
    
    def getDataTopic(self, channel):
        return "%s/data/%s" % (self.rootTopic, channel)
    
    def virtualWrite(self, channel, value, dataType, dataUnit):
        if (self.connected):
            topic = self.getDataTopic(channel)
            payload = "%s,%s=%s" % (dataType, dataUnit, value)        
            self.mqttPublish(topic, payload)
    
    def celsiusWrite(self, channel, value):
        self.virtualWrite(channel, value, TYPE_TEMPERATURE, UNIT_CELSIUS)

    def fahrenheitWrite(self, channel, value):
        self.virtualWrite(channel, value, TYPE_TEMPERATURE, UNIT_FAHRENHEIT)

    def kelvinWrite(self, channel, value):
        self.virtualWrite(channel, value, TYPE_TEMPERATURE, UNIT_KELVIN)
    
    def luxWrite(self, channel, value):
        self.virtualWrite(channel, value, TYPE_LUMINOSITY, UNIT_LUX)
    
    def pascalWrite(self, channel, value):
        self.virtualWrite(channel, value, TYPE_BAROMETRIC_PRESSURE, UNIT_PASCAL)
    
    def hectoPascalWrite(self, channel, value):
        self.virtualWrite(channel, value, TYPE_BAROMETRIC_PRESSURE, UNIT_HECTOPASCAL)

