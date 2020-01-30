#!/usr/bin/env python

import rospy
import geometry_msgs.msg

p = geometry_msgs.msg.PointStamped()
p.point.x = 1
p.point.y=2
p.point.z=3

print p.__getattribute__('point')
print p.__getattribute__('point').__getattribute__('y')
s = p._full_text
print type(s.splitlines()[0])
final_str = str()
u = str()
for i in s.splitlines():
	u = i + '\n'
	if "x" in i:
		u = i + ': ' + str(p.__getattribute__('point').__getattribute__('x')) + '\n'
	elif "y" in i:
		u = i + ': ' + str(p.__getattribute__('point').__getattribute__('y')) + '\n'
	elif "z" in i:
		u = i + ': ' + str(p.__getattribute__('point').__getattribute__('z')) + '\n'
	final_str = final_str + u
print final_str

