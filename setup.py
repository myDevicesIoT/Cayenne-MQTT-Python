from setuptools import setup

setup(name             = 'Cayenne',
      version          = '1.0',
      author           = 'myDevices',
      author_email     = 'N/A',
      description      = 'Cayenne MQTT Python Library',
      long_description = 'The Cayenne MQTT Python Library provides functions to easily connect to the Cayenne IoT project builder.',
      license          = 'MIT',
      keywords         = 'myDevices Cayenne MQTT',
      url              = 'https://github.com/myDevicesIoT/Cayenne-MQTT-Python',
      packages         = ['cayenne'],
      install_requires = [
        'paho-mqtt',
      ],
      )
