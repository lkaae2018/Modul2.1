echo Packet Tracer 7.2 til Linux skal downloads fra følgende adresse:
echo https://drive.google.com/file/d/1BQNYBCwADYlOpJ4gYA9rTl2U14j5RpUE/view
echo Tryk på linket og kopier og derefter download filen i biblioteket Hentet!
echo
echo Tryk på en tast for at forsætte!
read m
mkdir PT72Installer
sudo tar xvzf 'Packet Tracer 7.2 for Linux 64 bit.tar.gz' -C PT72Installer
cd PT72Installer
./install
sudo reboot
