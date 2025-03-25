import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts

class SquareClient(Node):
    def __init__(self):
        super().__init__('square_client')
        self.cli = self.create_client(
            AddTwoInts,
            'square_number'
        )
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Esperando servicio "square_number"...')

    def send_request(self, number):
        req = AddTwoInts.Request()
        req.a = number 
        req.b = 0
        future = self.cli.call_async(req)
        return future


def main(args=None):
    rclpy.init(args=args)
    client = SquareClient()
    future = client.send_request(5)  # Por ej, llamo al 5
    rclpy.spin_until_future_complete(client, future)
    if future.result() is not None:
        print(f'Resultado: {future.result().sum}')
    else:
        client.get_logger().info('Error al llamar al servicio.')
    rclpy.shutdown()


if __name__ == '__main__':
    main()
