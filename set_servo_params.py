# Script for testing 5.0V 20ms servo motor connected to ROSbot 2R
import rclpy
from time import sleep
from rclpy.node import Node
from rcl_interfaces.srv import SetParameters
from rcl_interfaces.msg import Parameter, ParameterType

class ParameterSetterNode(Node):
    def __init__(self):
        super().__init__('servo_tester')

        self.set_parameters_client = self.create_client(
            SetParameters, '/rosbot_ros2_firmware/set_parameters')

        while not self.set_parameters_client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
        self.get_logger().info('Service available!')

    def set_parameters(self):
        request = SetParameters.Request()
        servo_voltage = Parameter()
        servo_voltage.name = 'servo_voltage'
        servo_voltage.value.type = ParameterType.PARAMETER_DOUBLE
        servo_voltage.value.double_value = 5.0
        request.parameters.append(servo_voltage)

        servo_enable_power = Parameter()
        servo_enable_power.name = 'servo_enable_power'
        servo_enable_power.value.type = ParameterType.PARAMETER_BOOL
        servo_enable_power.value.bool_value = True
        request.parameters.append(servo_enable_power)

        servo0_enable = Parameter()
        servo0_enable.name = 'servo0_enable'
        servo0_enable.value.type = ParameterType.PARAMETER_BOOL
        servo0_enable.value.bool_value = True
        request.parameters.append(servo0_enable)

        servo0_period = Parameter()
        servo0_period.name = 'servo0_period'
        servo0_period.value.type = ParameterType.PARAMETER_INTEGER
        servo0_period.value.integer_value = 20000
        request.parameters.append(servo0_period)

        future = self.set_parameters_client.call_async(request)
        while not future.done():
            rclpy.spin_once(self, timeout_sec=1.0)
            future = self.set_parameters_client.call_async(request)
            sleep(10.0)
        if future.result() is not None:
            self.get_logger().info('Parameters set successfully')
        else:
            self.get_logger().error('Failed to set parameters')


def main(args=None):
    rclpy.init(args=args)
    node = ParameterSetterNode()
    node.set_parameters()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
