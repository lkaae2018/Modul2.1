cd /opt/pt/bin
./PacketTracer7
cd /tmp
wget http://ftp.us.debian.org/debian/pool/main/libp/libpng/libpng12-0_1.2.50-2+deb8u3_amd64.deb
sudo dpkg -i libpng12-0_1.2.50-2+deb8u3_amd64.deb

cd /opt/pt/bin
./PacketTracer7

sudo apt update && sudo apt install libqt5webkit5 libqt5multimediawidgets5
 libqt5svg5 libqt5script5 libqt5scripttools5 libqt5sql5

cd /opt/pt/bin
./PacketTracer
