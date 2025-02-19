#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist

def callback(data):
    rospy.loginfo(f"Received: {data.data}")
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    twist = Twist()

    if data.data == "Maju":
        twist.linear.x = 2.0
    elif data.data == "Mundur": # Jika pesan yang diterima adalah "Mundur"
        twist.linear.x = -2.0  # Kecepatan linear -2.0
    elif data.data == "Kiri": # Jika pesan yang diterima adalah "Kiri"
        twist.angular.z = 2.0  # Kecepatan angular 2.0
    elif data.data == "Kanan": # Jika pesan yang diterima adalah "Kanan"
        twist.angular.z = -2.0  # Kecepatan angular -2.0
    else:
        rospy.loginfo("Perintah tidak dikenal")
        return

    pub.publish(twist)

def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber('/chatter', String, callback)
    rospy.spin()

if __name__ == '__main__':
    try:
        listener()
    except rospy.ROSInterruptException:
        pass
