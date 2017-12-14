"""
This module contains the data types used when sending data to the Cayenne server.
"""

# Data types
TYPE_ACCELERATION = 'accel' # Acceleration, units: UNIT_G
TYPE_ANALOG_ACTUATOR = 'analog_actuator' # Analog Actuator, units: UNIT_ANALOG
TYPE_ANALOG_SENSOR = 'analog_sensor' # Analog Sensor, units: UNIT_ANALOG
TYPE_BAROMETRIC_PRESSURE = 'bp' # Barometric pressure, units: UNIT_PASCAL, UNIT_HECTOPASCAL
TYPE_BATTERY = 'batt' # Battery, units: UNIT_PERCENT, UNIT_RATIO, UNIT_VOLTS
TYPE_CO2 = 'co2' # Carbon Dioxide, units: UNIT_PPM
TYPE_COUNTER = 'counter' # Counter, units: UNIT_ANALOG
TYPE_CURRENT = 'current' # Current, units: UNIT_AMP, UNIT_MAMP
TYPE_DIGITAL_ACTUATOR = 'digital_actuator' # Digital Actuator, units: UNIT_DIGITAL
TYPE_DIGITAL_SENSOR = 'digital_sensor' # Digital Sensor, units: UNIT_DIGITAL
TYPE_ENERGY = 'energy' # Energy, units: UNIT_KWH
TYPE_EXT_WATERLEAK = 'ext_wleak' # External Waterleak, units: UNIT_ANALOG
TYPE_FREQUENCY = 'freq' # Frequency, units: UNIT_HERTZ
TYPE_GPS = 'gps' # GPS, units: UNIT_GPS
TYPE_GYROSCOPE = 'gyro' # Gyroscope, units: UNIT_ROTATION_PER_MINUTE, UNIT_DEGREE_PER_SEC
TYPE_LUMINOSITY = 'lum' # Luminosity, units: UNIT_LUX, UNIT_VOLTS, UNIT_PERCENT, UNIT_RATIO
TYPE_MOTION = 'motion' # Motion, units: UNIT_DIGITAL
TYPE_POWER = 'pow' # Power, units: UNIT_WATT, UNIT_KILOWATT
TYPE_PROXIMITY = 'prox' # Proximity, units: UNIT_CENTIMETER, UNIT_METER, UNIT_DIGITAL
TYPE_RAIN_LEVEL = 'rain_level' # Rain Level, units: UNIT_CENTIMETER, UNIT_MILLIMETER
TYPE_RELATIVE_HUMIDITY = 'rel_hum' # Relative Humidity, units: UNIT_PERCENT, UNIT_RATIO
TYPE_RESISTANCE = 'res' # Resistance, units: UNIT_OHM
TYPE_RSSI = 'rssi' # Received signal strength indicator, units: UNIT_DBM
TYPE_SNR = 'snr' # Signal Noise Ratio, units: UNIT_DB
TYPE_SOIL_MOISTURE = 'soil_moist' # Soil Moisture, units: UNIT_PERCENT
TYPE_SOIL_PH = 'soil_ph' # Soil pH, units: UNIT_ANALOG
TYPE_SOIL_WATER_TENSION = 'soil_w_ten' # Soil Water Tension, units: UNIT_KILOPASCAL, UNIT_PASCAL
TYPE_TANK_LEVEL = 'tl' # Tank Level, units: UNIT_ANALOG
TYPE_TEMPERATURE = 'temp' # Temperature, units: UNIT_FAHRENHEIT, UNIT_CELSIUS, UNIT_KELVIN
TYPE_VOLTAGE = 'voltage' # Voltage, units: UNIT_VOLTS, UNIT_MILLIVOLTS
TYPE_WIND_SPEED = 'wind_speed' # Wind Speed, units: UNIT_KM_PER_H

# Unit types
UNIT_UNDEFINED = 'null' # Undefined unit type
UNIT_AMP = 'a' # Ampere
UNIT_ANALOG = 'null' # Analog
UNIT_CELSIUS = 'c' # Celsius
UNIT_CENTIMETER = 'cm' # Centimeter
UNIT_DB = 'db' # Decibels
UNIT_DBM = 'dbm' # dBm
UNIT_DEGREE_PER_SEC = 'dps' # Degree per second
UNIT_DIGITAL = 'd' # Digital (0/1)
UNIT_FAHRENHEIT = 'f' # Fahrenheit
UNIT_G = 'g' # Acceleration
UNIT_GPS = 'm' # GPS
UNIT_HECTOPASCAL = 'hpa' # Hectopascal
UNIT_HERTZ = 'hz' # Hertz
UNIT_KELVIN = 'k' # Kelvin
UNIT_KILOPASCAL = 'kpa' # Kilopascal
UNIT_KILOWATT = 'kw' # Kilowatts
UNIT_KM_PER_H = 'kmh' # Kilometer per hour
UNIT_KWH = 'kwh' # Killowatt Hour
UNIT_LUX = 'lux' # Lux
UNIT_MAMP = 'ma' # Milliampere
UNIT_METER = 'm' # Meter
UNIT_MILLIMETER = 'mm' # Millimeter
UNIT_MILLIVOLTS = 'mv' # Millivolts
UNIT_OHM = 'ohm' # Ohm
UNIT_PASCAL = 'pa' # Pascal
UNIT_PERCENT = 'p' # Percent (%)
UNIT_PPM = 'ppm' # Parts per million
UNIT_RATIO = 'r' # Ratio
UNIT_ROTATION_PER_MINUTE = 'rpm' # Rotation per minute
UNIT_VOLTS = 'v' # Volts
UNIT_WATT = 'w' # Watts