#!/usr/bin/env python
import rospy
from trajectory_smoothing_msg.msg import *
from velocity_extraction_msg.msg import *
from velocity_extraction_msg.srv import *

pub = None

def callback(msg):
	print "Received the points"
	rospy.wait_for_service('velocity_from_points')
	global pub
	try:
		vel = rospy.ServiceProxy('velocity_from_points', TwistFromPoints)
		res = vel(msg)
		pub.publish(res.velocity)
		# print "Published the velocity"
	except rospy.ServiceException, e:
		print "Service call failed: %s"%e


def main():
	rospy.init_node('velocity_from_points')
	global pub
	pub = rospy.Publisher("final_topic", TwistFromPoint, queue_size=1000)
	sub = rospy.Subscriber("trajectory_points", SmoothRWristCoordsWithRespectToBase, callback)
	rospy.spin()





if __name__ == "__main__":
	main()