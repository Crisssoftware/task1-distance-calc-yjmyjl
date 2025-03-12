import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose
from math import pow, sqrt
from std_msgs.msg import String


class MinimalSubscriber(Node):



    def __init__(self):
        super().__init__('turtle_distance')
        self.subscription = self.create_subscription(Pose,'turtle1/pose', self.listener_callback,10)
        self.subscription  # prevent unused variable warning
        
        self.publisher_ = self.create_publisher(String, 'turtle1/distance_from_origin', 10)
        timer_period = 0.1  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
            
        self.x = 0.0
        self.y = 0.0
        self.comp = 0.0
    	
    def listener_callback(self, msg):
        self.x = msg.x
        self.y = msg.y
        
    def timer_callback(self):
        msg = String()
        self.comp =  sqrt(pow(self.x,2) + pow(self.y,2)) 
        msg.data = '%f' % self.comp
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)


def main(args=None):
    rclpy.init(args=args)

    turtle_distance = MinimalSubscriber()

    rclpy.spin(turtle_distance)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    turtle_distance.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
