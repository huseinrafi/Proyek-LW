#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def talker():
    pub = rospy.Publisher('/chatter', String, queue_size=10)  # Membuat publisher ke topic 'chatter'
    rospy.init_node('talker', anonymous=True)  # Inisialisasi node dengan nama 'talker'
    rate = rospy.Rate(1)  # Frekuensi pengiriman pesan (1 Hz = 1 detik sekali)

    while not rospy.is_shutdown():
        input_message = input("Masukkan Perintah untuk menggerakkan Turtle (Maju, Mundur, Kiri, Kanan)")  # Meminta input pesan dari user  
        message = String()  # Membuat objek message dengan tipe data String
        message.data = input_message # Mengisi data message dengan input dari user
        rospy.loginfo(f"Sending: {message.data}")
        pub.publish(message.data)
        rate.sleep()  # Tunggu sesuai rate

if __name__ == "__main__":
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
