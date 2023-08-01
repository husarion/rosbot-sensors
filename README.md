# rosbot-sensors
Visualization for ROSbot 2R, ROSbot 2 PRO and ROSbot 2.0 sensors.

# Quick Start
## On PC
### Clone the repository:
```
git clone https://github.com/husarion/rosbot-sensors
cd rosbot-sensors
```
### Configure workspace:
In `.env` file you can change the lidar baudrate and enable the mecanum controller.

### Sync with robot:
Sync workspace with ROSbot:
```
./sync_with_rosbot.sh <ROSbot_ip>
```

## On ROSbot
In the ROSbot's shell execute (in the `/home/husarion/rosbot-sensors` directory):
```
docker compose up
```

# On PC
### Open Foxglove application in browser:
Open web browser and go to `<ROSbot_ip>:8080` website. Chrome/Chromium browser is highly recommended.

# Demo
Now reload the Foxglove website inside your web browser on your PC. You should see the Foxglove application. Click on left top button `Data source`, click the plus `new connection` -> `Open connection` and you should see `WebSocket URL` set to `ws://<ROSbot_ip>:9090` > `Open`. You can see step by step instructions below.

![foxglove_sensors](.docs/foxglove_connect.gif)
