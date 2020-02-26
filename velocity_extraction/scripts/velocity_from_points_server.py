#!/usr/bin/env python
import rospy
from trajectory_smoothing_msg.msg import *
from velocity_extraction_msg.msg import *
from geometry_msgs.msg import TwistStamped
# import velocity_extraction.srv
from velocity_extraction_msg.srv import TwistFromPoints
from scipy.spatial import distance

dt = 0.2

def handle_vel(req):
	global dt
	points = req.points.points
	final_vel = TwistFromPoint()
	print (len(points))
	for i in range(len(points)-1):
		vel = TwistStamped()
		# print points[i]
		a = (points[i].x, points[i].y, points[i].z)
		b = (points[i+1].x, points[i+1].y, points[i+1].z)
		c = 10*distance.euclidean(a,b)
		if c == 0:
			continue
		vel.twist.linear.x = (points[i+1].x-points[i].x)/c
		vel.twist.linear.y = (points[i+1].y-points[i].y)/c
		vel.twist.linear.z = (points[i+1].z-points[i].z)/c
		vel.header.stamp = rospy.Time(i*c)
		final_vel.twistArray.append(vel)
		final_vel.d.append(c)
	return final_vel

if __name__ == "__main__":
	rospy.init_node("velocity_from_points_server")
	s = rospy.Service("velocity_from_points", TwistFromPoints, handle_vel)
	rospy.spin()