from gpiozero import MCP3008
import time
adc = MCP3008(channel=0)

while True:
    voltage = adc.voltage
    print("Spaendningen er: ", voltage)
    time.sleep(1)
