#!/bin/bash

# Create a temporary file for the script
TMP_SCRIPT="/tmp/ros2_script.sh"

# Write the script content to the temporary file
cat <<EOF > $TMP_SCRIPT
#!/bin/bash

# Waiting for the service to become available
while ! ros2 service list | grep "/rosbot_ros2_firmware/set_parameters"; do
    echo "service not available, waiting again..."
    sleep 1
done

echo "Service available!"

# Setting the parameters
ros2 param set /rosbot_ros2_firmware servo_voltage 5.0
ros2 param set /rosbot_ros2_firmware servo_enable_power true
ros2 param set /rosbot_ros2_firmware servo0_enable true
ros2 param set /rosbot_ros2_firmware servo0_period 20000

# Check if the parameters are set correctly
if ros2 param get /rosbot_ros2_firmware servo_voltage && \
   ros2 param get /rosbot_ros2_firmware servo_enable_power && \
   ros2 param get /rosbot_ros2_firmware servo0_enable && \
   ros2 param get /rosbot_ros2_firmware servo0_period; then
    echo "Parameters set successfully"
else
    echo "Failed to set parameters"
fi
EOF

# Make the script executable
chmod +x $TMP_SCRIPT

# Run the Docker container with the script mounted as a volume
docker run -it --rm -v $TMP_SCRIPT:$TMP_SCRIPT ros:humble-ros-core $TMP_SCRIPT

# Clean up the temporary script (optional)
rm $TMP_SCRIPT
