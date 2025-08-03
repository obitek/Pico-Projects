
from machine import ADC, Pin
import time

pot = ADC(Pin(26))       # Initialize ADC on GP26 (ADC0)

while True:
    raw_value = pot.read_u16()           # Read ADC value (0-65535 for 16-bit resolution)
    voltage = (raw_value / 65535) * 3.3  # Convert to voltage (assuming 3.3V reference)
    print(f"Raw: {raw_value}, Voltage: {voltage:.2f}V")
    time.sleep(0.5)      # Delay for readability
