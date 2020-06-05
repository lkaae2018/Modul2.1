import thingspeak
import time
import Adafruit_DHT
 
channel_id = 206897 # PUT CHANNEL ID HERE
write_key  = '24GJQV17H7H4XGJ5' # PUT YOUR WRITE KEY HERE
read_key   = '9EZ7E0918UVVAGAY' # PUT YOUR READ KEY HERE
pin = 5
sensor = Adafruit_DHT.DHT22
 
def measure(channel):
    try:
        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
        # write
        response = channel.update({'field5': temperature, 'field6': humidity})
        
        # read
        read = channel.get({})
        print("Read:", read)
        
    except:
        print("connection failed")
 
 
if __name__ == "__main__":
    channel = thingspeak.Channel(id=channel_id, write_key=write_key, api_key=read_key)
    while True:
        measure(channel)
        # free account has an api limit of 15sec
        time.sleep(15)