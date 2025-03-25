import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts

class SquareService(Node):
    def __init__(self):
        super().__init__('square_service')
        self.srv = self.create_service(
            AddTwoInts,
            'square_number',
            self.square_callback
        )

    def square_callback(self, request, response):
        self.get_logger().info(f'Recibido número: {request.a}')
        response.sum = request.a * request.a  # Cuadrado del número
        return response


def main(args=None):
    rclpy.init(args=args)
    node = SquareService()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
