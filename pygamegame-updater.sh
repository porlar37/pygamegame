#!/bin/bash
cd /
sudo mkdir pygamegame
wget https://codeload.github.com/porlar37/pygamegame/zip/master
sudo rm /pygame
sudo mkdir pygamegame
sudo apt-get install unzip
unzip pygamegame-master -p /pygamegame

