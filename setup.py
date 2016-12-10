from setuptools import setup
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as readme:
    long_description = readme.read()

classifiers = ['Development Status :: 3 - Alpha',
               'Operating System :: MacOS :: MacOS X',
               'Operating System :: Microsoft :: Windows',
               'Operating System :: POSIX',
               'Programming Language :: Python',
               'License :: OSI Approved :: MIT License',
               'Intended Audience :: Developers',
               'Programming Language :: Python',
               'Programming Language :: Python :: 2.7',
               'Programming Language :: Python :: 3',
               'Topic :: Software Development',
               'Topic :: Communications',
               'Topic :: Internet',
               'Topic :: Home Automation',
               'Topic :: System :: Monitoring']
               
setup(name             = 'cayenne-mqtt',
      version          = '1.0.0',
      author           = 'myDevices',
      author_email     = 'N/A',
      description      = 'Cayenne MQTT Python Library',
      long_description = long_description,
      license          = 'MIT',
      keywords         = 'myDevices Cayenne MQTT',
      url              = 'https://github.com/myDevicesIoT/Cayenne-MQTT-Python',
      classifiers      = classifiers,
      packages         = ['cayenne-mqtt'],
      install_requires = [
        'paho-mqtt',
      ],
      )
