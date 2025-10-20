import rclpy
from rclpy.node import Node

from msg_package.msg import Broadcast


class ExamplePublisher(Node):

    def __init__(self):
        super().__init__('publish_information')
        self.publisher_ = self.create_publisher(Broadcast, 'topic', 10)
        timer_period = 0.5  
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = Broadcast()
        msg.num = self.i
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)
        self.i += 1


def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = ExamplePublisher()

    rclpy.spin(minimal_publisher)

    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()