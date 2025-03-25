import rclpy
from rclpy.node import Node
from sensor_msgs.msg import NavSatFix
import random
import time

class GPSPublisher(Node):
    def __init__(self):
        super().__init__('uav_publisher')
        self.publisher_ = self.create_publisher(NavSatFix, 'drone/gps', 10)
        self.timer = self.create_timer(1.0, self.publish_gps_data)

    def publish_gps_data(self):
        msg = NavSatFix()

        # Datos GPS
        msg.latitude = random.uniform(-90.0, 90.0)  # latitud aleatoria
        msg.longitude = random.uniform(-180.0, 180.0)  # longitud aleatoria
        msg.altitude = random.uniform(0.0, 10000.0)  # altitud aleatoria

        # Publicar los datos de GPS
        self.publisher_.publish(msg)
        self.get_logger().info(f"Publicando datos de GPS: Latitud: {msg.latitude}, Longitud: {msg.longitude}, Altitud: {msg.altitude}")

def main(args=None):
    rclpy.init(args=args)
    uav_publisher = GPSPublisher()
    rclpy.spin(uav_publisher)

    uav_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
