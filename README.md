# rosbot-sensors
Visualization for ROSbot 2R, ROSbot 2 PRO and ROSbot 2.0 sensors.

## Quick start

**1. Connect to your ROSbot via ssh.**

```bash title="user@device:~$"
ssh husarion@<ROSBOT_IP/HUSARNET_NAME>
```

**2. Clone the repository on your ROSbot.**

```bash title="husarion@husarion:~$"
git clone https://github.com/husarion/rosbot-sensors
cd rosbot-sensors
```

**3. Flash firmware.**

```bash title="husarion@husarion:~$"
docker stop rosbot microros || true && \
docker run --rm -it --privileged \
husarion/rosbot:humble-0.6.1-20230712 \
/flash-firmware.py /root/firmware.bin
```

**4. Run Docker Compose.**

```bash title="husarion@husarion:~/rosbot-xl-sensors$"
docker compose up
```

**5. Open Foxglove application in browser.**

To access Foxglove, input the following in your browser's search bar:

- `http://<localhost>:8080/ui` - if you work locally,
- `http://<ROSBOT_IP>:8080/ui` - if you want to connect to a device connected to the same LAN,
- `http://<HUSARNET_NAME>:8080/ui` - if you want to connect to the device using Husarnet VPN.

> [!NOTE]
> You should use the **Chrome/Chromium** browser and wait a few seconds after running docker-compose to ensure all images boot up correctly.

### Result

<div style={{width: '85%', margin: 'auto'}}>

![](/img/other/foxglove_xl_result.gif)

</div>

![foxglove_result](.docs/foxglove_xl_result.gif)