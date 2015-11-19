from station_geometry import station_geometry
from event import event
from matplotlib import pyplot as plt
import numpy as np
import math
from math import sin, cos
from mpl_toolkits.mplot3d import Axes3D
#import sys

#Initialize station_geometry
station = station_geometry(2)

#Station information
station2_x = np.empty((5,4), dtype = float)
station2_y = np.empty((5,4), dtype = float)
station2_z = np.empty((5,4), dtype = float)
station3_strings = []

#Gets the location for every antenna
#loops through strings
for i in range(5):
	#loops through antennas
	for j in range(4):
		station2_x[i][j] = station.get_string_coordinates(2,i+1, j)[0]
		station2_y[i][j] = station.get_string_coordinates(2,i+1, j)[1]
		station2_z[i][j] = station.get_string_coordinates(2,i+1, j)[2]

#Surface for visualization
#Initialize figure and 3D plot
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.set_zlim3d(-4000,10)
ax.set_ylim3d(-3000,3000)
ax.set_xlim3d(-3000,3000)
#Create event at 56 degrees
e = event()
#vp, dv, oca, d = e.create_vertex()
while True:
	vp, dv, oca, d = e.create_vertex()
	s = 0.0
	for i in range(4):
		for j in range(4):
			s += oca[i][j]
	s = s/16.0
	if s > 55.5 and s < 56.5:
		break
	else:
		pass

print oca

#Loop through each detector and set color
#Then plots the event vertex and direction
#Lines are plotted connecting the detectors to the vertex for visualization
for i in range(4):
	#conditionals plot detectors
	#Sets legend entry once
	if i == 0:
		ax.scatter(station2_x[i][0], station2_y[i][0], station2_z[i][0], c='r', label='Verticle Antenna')
		ax.scatter(station2_x[i][2], station2_y[i][2], station2_z[i][2], c='r')#, marker="|")
		ax.scatter(station2_x[i][1], station2_y[i][1], station2_z[i][1], c='g', label='Horizontal Antenna')
		ax.scatter(station2_x[i][3], station2_y[i][3], station2_z[i][3], c='g')#, marker="_")
	else:
		ax.scatter(station2_x[i][0], station2_y[i][0], station2_z[i][0], c='r')#, marker="|")
		ax.scatter(station2_x[i][2], station2_y[i][2], station2_z[i][2], c='r')#, marker="|")
		ax.scatter(station2_x[i][1], station2_y[i][1], station2_z[i][1], c='g')#, marker="_")
		ax.scatter(station2_x[i][3], station2_y[i][3], station2_z[i][3], c='g')#, marker="_")
	#Connect the detectors to the vertex
	ax.plot((vp[0], station2_x[i][0]), (vp[1], station2_y[i][0]), (vp[2], station2_z[i][0]), c='r')#, marker="|")
	ax.plot((vp[0],station2_x[i][2]), (vp[1],station2_y[i][2]), (vp[2],station2_z[i][2]), c='r')#, marker="|")
	ax.plot((vp[0],station2_x[i][1]), (vp[1],station2_y[i][1]), (vp[2],station2_z[i][1]), c='g')#, marker="_")
	ax.plot((vp[0],station2_x[i][3]), (vp[1],station2_y[i][3]), (vp[2],station2_z[i][3]), c='g')#, marker="_")
#Plot pulsers
ax.scatter(station2_x[4][0], station2_y[4][0], station2_z[4][0], c='g')#, marker="|")
ax.scatter(station2_x[4][1], station2_y[4][1], station2_z[4][1], c='r')#, marker="_")
ax.scatter(station2_x[4][2], station2_y[4][2], station2_z[4][2], c='g')#, marker="|")
ax.scatter(station2_x[4][3], station2_y[4][3], station2_z[4][3], c='r')#, marker="_")

#Plotting and labeling
#Vertex and direction vector
ax.scatter(vp[0], vp[1], vp[2], label='Vertex')
ax.scatter(dv[0], dv[1], dv[2], c='g', marker='^', label='Direction')
ax.plot((vp[0],dv[0]),(vp[1],dv[1]),(vp[2],dv[2]))
#ax.text(0, 0, 10, "Surface", color='red')
ax.set_zlabel('Depth (m)')
ax.set_xlabel('Position From Center (m)')
ax.set_ylabel('Position From Center (m)')
ax.legend()
ax.set_title('ARA02')
plt.show()
#plt.savefig('Images/Plots/Cone0' + sys.argv[1] + '.png')
