import thingspeak
import time

channel_id = 1049013 # PUT CHANNEL ID HERE
write_key='B530FR63JBR4S3MN' # PUT YOUR WRITE KEY HERE
read_key='BQE5HYPZ0YTXJULT' # PUT YOUR READ KEY HERE

def thermometer():
          
              
    try:
        #callableculate CPU temperature of Raspberry Pi in Degrees C
        temp = int(open('/sys/class/thermal/thermal_zone0/temp').read()) / 1e3 # Get Raspberry Pi CPU temp
        params= channel.update({'field5': temp, 'key':key })
        print(temp)
                #print response.status, response.reason
               
        time.sleep(10)
                
    except:
        print ("connection failed")
        
if __name__ == "__main__":
    channel = thingspeak.Channel(id=channel_id, write_key = write_key, api_key = read_key)
    while True:
        thermometer()
        time.sleep(15)
 

