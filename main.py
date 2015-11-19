from station_geometry import station_geometry
from event import event
from matplotlib import pyplot as plt
import numpy as np
import math
from math import sin, cos
import sys
import subprocess

#Pass arguement "save" to save figure
save_file = False
if len(sys.argv) > 1:
	if sys.argv[1] == 'save':
		save_file = True
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

#Event object
e = event()
#While loop finds optimal event
#vp, dv, oca, d = e.create_vertex()
#Comment out to find complete random event

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

progress_display = 0.0
file_name = 'Images/Plots/shower_test.dat'
fig, ax = plt.subplots(4,4, sharex=True, sharey=True)
for i in range(4):
	for j in range(4):
		#Call MC w/ createAskSingleAngle.cpp with E=100EeV
		subprocess.call(['./createAsk', '10000000000', str(oca[i][j]), 'test'])
		n = 's'+str(i)+'d'+str(j)+'_'+str(int(oca[i][j]))
		data = np.fromfile(file=file_name, dtype=float, sep='\n')
		ax[i][j].plot(np.multiply((1/d[i][j]),data), label=n)
		progress_display += 6.25
		print str(progress_display) + '%',
		print '\b'*8,
		sys.stdout.flush()
plt.xlim([8550, 8800])
plt.show()
if save_file == True:
	fig.savefig('Images/Plots/Hit_100EeV_' + str(int(d[0][0])) +'m.png')
