



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








