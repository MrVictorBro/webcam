

https://janus.conf.meetecho.com/videoroomtest.html
https://janus.conf.meetecho.com/devicetest.html


--1 установка виртуальной веб камеры
--Аналог Splitcam в Linux
https://www.dr.arut.ru/analog-splitcam-v-linux/

git clone https://github.com/umlaeute/v4l2loopback.git
cd v4l2loopback
sudo make
sudo make install
sudo depmod -a
sudo modprobe v4l2loopback

ls /dev/video*

wget https://yadi.sk/d/dTLrFJAfhNvqow

ffmpeg -re -i video.mp4 -threads 0 -f v4l2 /dev/video0

--2 установка драйвера chome
https://chromedriver.chromium.org/downloads

wget https://chromedriver.storage.googleapis.com/2.41/chromedriver_linux64.zip
sudo apt install unzip
unzip chromedriver_linux64.zip

sudo mv chromedriver /usr/bin/chromedriver
sudo chown root:root /usr/bin/chromedriver
sudo chmod +x /usr/bin/chromedriver


--3 установка хрома

sudo curl -sS -o - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add
sudo echo "deb [arch=amd64]  http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list
sudo apt-get -y update
sudo apt-get -y install google-chrome-stable









