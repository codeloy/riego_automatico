from machine import Pin
import dht

# Sensor DHT22
sensor_dht = dht.DHT22(Pin(4))

def leer_dht():
    sensor_dht.measure()
    return {
        'temperatura': sensor_dht.temperature(),
        'humedad_aire': sensor_dht.humidity()
    }
print(leer_dht())