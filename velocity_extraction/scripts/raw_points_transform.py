#!/usr/bin/env python
import rospy
from moveit_motion_replication_msgs.msg import *
from velocity_extraction_msg.msg import *
from velocity_extraction_msg.srv import *
from geometry_msgs.msg import Point
from keypoint_3d_matching_msgs.msg import *

pub = None
points_raw = SmoothRWristCoordsWithRespectToBase()
seconds = 111111111111111111111111111111

def callback(data):
	global points_raw, seconds
	# print "Received the points"
	for i in range(len(data.keypoints)):
		if (data.keypoints[i].name == "RWrist"):
			point_raw = Point()
			point_raw.x = data.keypoints[i].points.point.x
			point_raw.y = data.keypoints[i].points.point.y
			point_raw.z = data.keypoints[i].points.point.z
			seconds = rospy.get_time()
			points_raw.points.append(point_raw)
			continue


def main():
	rospy.init_node('velocity_from_points')
	global pub, seconds, points_raw
	pub = rospy.Publisher("trajectory_points", SmoothRWristCoordsWithRespectToBase, queue_size=1000)
	sub = rospy.Subscriber("topic_transform", Keypoint3d_list, callback)
	while rospy.get_time() - seconds < 1:
		pass	
	print "Publish the points"
	pub.publish(points_raw)	
	rospy.spin()





if __name__ == "__main__":
	main()