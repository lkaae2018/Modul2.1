echo nu hentets den sidste nye version af playonlinux
git clone https://github.com/PlayOnLinux/POL-POM-4
echo Nu installeres den!!!!!
echo
wget -q "http://deb.playonlinux.com/public.gpg" -O- | sudo apt-key add -
sudo wget http://deb.playonlinux.com/playonlinux_cosmic.list -O /etc/apt/sources.list.d/playonlinux.list
sudo apt-get update
sudo apt-get install playonlinux
