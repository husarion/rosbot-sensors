#!/bin/bash

echo "stopping all running containers"
docker stop $(docker ps -q)

echo "flashing the firmware for STM32 microcontroller in ROSbot"
docker run \
--rm -it --privileged \
$(yq .services.rosbot.image compose.yaml) \
/flash-firmware.py /root/firmware.bin
