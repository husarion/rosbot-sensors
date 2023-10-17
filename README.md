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

> **`yq` required**
>
> Make sure `yq` is installed, by executing the script:
>
> ```bash title="husarion@husarion:~$"
> sudo ./install_yq.sh
> ```

**3. Flash firmware.**

```bash title="husarion@husarion:~$"
./flash_rosbot_firmware.sh
```

**4. Run Docker Compose.**

```bash title="husarion@husarion:~/rosbot-xl-sensors$"
docker compose up
```

**5. Enable Servos.**

```bash title="husarion@husarion:~/rosbot-xl-sensors$"
./set_servo_params.sh
```

**6. Open Foxglove application in browser.**

To access Foxglove, input the following in your browser's search bar:

- `http://<localhost>:8080/ui` - if you work locally,
- `http://<ROSBOT_IP>:8080/ui` - if you want to connect to a device connected to the same LAN,
- `http://<HUSARNET_NAME>:8080/ui` - if you want to connect to the device using Husarnet VPN.

> [!NOTE]
> You should use the **Chrome/Chromium** browser and wait a few seconds after running `docker compose` to ensure all images boot up correctly.

### Result

![foxglove_result](.docs/foxglove_result.gif)

