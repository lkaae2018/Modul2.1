sudo apt update
sudo apt upgrade
echo Nu er RPi opdateret!!
echo
echo
echo SPI&VNC skal enables under interfaces!!
sudo raspi-config
echo Nu installeres modulerne til PMOD & BME680 
echo

sudo apt-get install python-pip python-dev libfreetype6-dev libjpeg-dev build-essential

sudo pip install designspark.pmod

curl https://get.pimoroni.com/i2c | bash

echo Nu installeres sw til BME680 luftkvalitetsmåler
echo


git clone https://github.com/pimoroni/bme680
cd bme680/library
sudo python setup.py install
sudo pip install bme680
curl https://get.pimoroni.com/bme680 | bash

