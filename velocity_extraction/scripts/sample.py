import sys
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d


x = list()
y = list()
z = list()
time=0
t = list()
file = open(sys.argv[1], "r")
fl = file.readlines()
flag = True
count = 0
# for i in range(len(fl)):
# 	if "secs" in fl[i] and 'n' not in fl[i]:
# 		time = 0.05*count
# 		count +=1
# 		print time
# 	if "x" in fl[i]:
# 		time = 0.05*count
# 		count +=1
# 		x.append(float(fl[i][11:-1]))
# 		y.append(float(fl[i+1][11:-1]))
# 		z.append(float(fl[i+2][11:-1]))
# 		t.append(time)

for i in range(len(fl)):
	if "secs" in fl[i] and 'n' not in fl[i]:
		time = 0.05*count
		count +=1
		print time
	if "linear" in fl[i]:
		print type(fl[i+1][11:-1])
		x.append(float(fl[i+1][11:-1]))
		y.append(float(fl[i+2][11:-1]))
		z.append(float(fl[i+3][11:-1]))
		t.append(time)
for i in x:
	print i

fig = plt.figure()
ax = plt.axes()
ax.set_xlabel("t")
ax.set_ylabel("x")
# ax.set_ylim(-0.01,0.02)
# ax.set_ylim(float(min(x)), float(max(x)))
ax.scatter(t,x)

fig = plt.figure()
ax = plt.axes()
ax.set_xlabel("t")
ax.set_ylabel("y")
# ax.set_ylim(-0.125,0.-0.105)
# ax.set_ylim(float(min(y)), float(max(y)))
ax.scatter(t,y)

fig = plt.figure()
ax = plt.axes()
ax.set_xlabel("t")
ax.set_ylabel("z")
# ax.set_ylim(-0.02,0.01)
# ax.set_ylim(float(min(z)), float(max(z)))
ax.scatter(t,z)

# fig = plt.figure()
# ax = plt.axes(projection='3d')
# ax.set_xlabel("x");
# ax.set_ylabel("y");
# ax.set_zlabel("z");
# ax.set_xlim(-0.5,0)
# ax.set_ylim(-0.5,0)
# ax.set_zlim(-0.5,0.5)
# ax.scatter3D(x, y, z)

# fig1 = plt.figure()
# ax1 = plt.axes(projection='3d')
# ax1.set_xlabel("x");
# ax1.set_ylabel("y");
# ax1.set_zlabel("z");
# # ax1.set_xlim(-0.5,0)
# # ax1.set_ylim(-0.5,0)
# # ax1.set_zlim(-0.5,0.5)
# ax1.scatter3D(x, y, z)
plt.show()

# print min(y), min(x), min(z)
# print max(y), max(x), max(z)
