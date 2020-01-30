#!/usr/bin/env python
import rospy
from trajectory_smoothing_msg.msg import *
from velocity_extraction_msg.msg import *
from geometry_msgs.msg import TwistStamped
# import velocity_extraction.srv
from velocity_extraction_msg.srv import TwistFromPoints

dt = 0.05

def handle_vel(req):
	global dt
	points = req.points.points
	final_vel = TwistFromPoint()
	print (len(points))
	for i in range(len(points)-1):
		vel = TwistStamped()
		print points[i]
		vel.twist.linear.x = (points[i+1].x-points[i].x)/dt
		vel.twist.linear.y = (points[i+1].y-points[i].y)/dt
		vel.twist.linear.z = (points[i+1].z-points[i].z)/dt
		vel.header.stamp = rospy.Time(i*dt)
		final_vel.twistArray.append(vel)
	return final_vel

if __name__ == "__main__":
	rospy.init_node("velocity_from_points_server")
	s = rospy.Service("velocity_from_points", TwistFromPoints, handle_vel)
	rospy.spin()