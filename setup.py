from setuptools import setup
from codecs import open
from os import path
from cayenne import __version__

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as readme:
    long_description = readme.read()

classifiers = ['Development Status :: 5 - Production/Stable',
               'Operating System :: MacOS :: MacOS X',
               'Operating System :: Microsoft :: Windows',
               'Operating System :: POSIX',
               'Programming Language :: Python',
               'License :: OSI Approved :: MIT License',
               'Intended Audience :: Developers',
               'Programming Language :: Python :: 2.7',
               'Programming Language :: Python :: 3.4',
               'Topic :: Software Development',
               'Topic :: Communications',
               'Topic :: Internet',
               'Topic :: Home Automation',
               'Topic :: System :: Monitoring']
               
setup(name             = 'cayenne-mqtt',
      version          = __version__,
      author           = 'myDevices',
      author_email     = 'support@mydevices.com',
      description      = 'Cayenne MQTT Python Library',
      long_description = long_description,
      license          = 'MIT',
      keywords         = 'myDevices Cayenne MQTT',
      url              = 'https://github.com/myDevicesIoT/Cayenne-MQTT-Python',
      classifiers      = classifiers,
      packages         = ['cayenne'],
      install_requires = [
        'paho-mqtt >= 1.3.0',
      ],
      )
