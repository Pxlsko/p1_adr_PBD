import rclpy
from rclpy.node import Node
from sensor_msgs.msg import NavSatFix

class GPSSubscriber(Node):
    def __init__(self):
        super().__init__('uav_subscriber')
        self.subscription = self.create_subscription(
            NavSatFix,
            'drone/gps',
            self.gps_callback,
            10
        )
        self.subscription

    def gps_callback(self, msg):
        self.get_logger().info(f"Recibido: Latitud: {msg.latitude}, Longitud: {msg.longitude}, Altitud: {msg.altitude}")

def main(args=None):
    rclpy.init(args=args)
    uav_subscriber = GPSSubscriber()
    rclpy.spin(uav_subscriber)

    uav_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
