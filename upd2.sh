#!/bin/bash
echo Nu opdateres Ubuntu 18.04
echo Tryk  1 for at forsætte eller 2 for at stoppe
read fts
echo $fts
echo 
if (($fts == 1)) ; then
	echo Opdatering start!!!
	sudo apt update
	sudo apt full-upgrade -y
	sudo apt autoremove -y
else 
	echo opdatering stopper!!
	exit
fi

