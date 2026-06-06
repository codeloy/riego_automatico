# sensors.py - Lectura de sensores
from machine import ADC, Pin

# Sensor humedad suelo (capacitivo, salida analogica)
# Calibrar: valor en SECO (~2254) y en AGUA (~95)
VALOR_SECO = 2254
VALOR_AGUA = 950

adc = ADC(Pin(34))
adc.atten(ADC.ATTN_11DB)   # Rango 0-3.3V

def leer_humedad_suelo():
    raw = adc.read()  # 0-4095
    # Convertir a porcentaje (invertido: mas humedo = menos voltaje)
    pct = (VALOR_SECO - raw) / (VALOR_SECO - VALOR_AGUA) * 100
    return max(0, min(100, round(pct, 1)))

print(leer_humedad_suelo())