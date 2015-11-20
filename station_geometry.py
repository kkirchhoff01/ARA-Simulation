import numpy as np

##############################################
#					     #
# This class assigns and provides access to  #
# all geometric information for the ARA02    #
# and ARA03 antenna clusters.		     #
# 					     #
##############################################

class station_geometry:
	def __init__(self, station=2):
		self.station_number=station
		#Detector keys
		self.detectors = {'TV': 0, 'BV': 1, 'TH': 2, 'BH': 3}
		#Holds the detector keys and the coordinates for each station
		self.stations = np.array([self.detectors, self.fill_coordinates(2), self.fill_coordinates(3) ])
	
	#Fills the coordinate information for the given station	
	def fill_coordinates(self,station=2):
		#List that holds X and Yposition of antennas
		string = np.empty(6, dtype=list)
		#Z positions of antennas
		DTV = np.empty(4, dtype=float)
		DBV = np.empty(4, dtype=float)
		DTH = np.empty(4, dtype=float)
		DBH = np.empty(4, dtype=float)
		DP = np.empty(4, dtype=float)
		#Holds coordinates of all antennas in 3D tuples
		station_coordinates = np.empty((5,4), dtype=list)
		#Conditional for seperate stations
		#ARA02
		if station == 2:
			#X,Y coordinates
			string[0] = [10.59,2.34]
			string[1] = [4.82, -10.38]
			string[2] = [-2.68, 8.68]
			string[3] = [-7.72, -4.47]
			string[4] = [37.87, -18.05]
			string[5] = [17.75, 35.34]
			#Z Coordinates
			#String 1
			DTV[0] = -170.41
			DBV[0] = -189.50
			DTH[0] = -167.49
			DBH[0] = -186.55
			#String 2
			DTV[1] = -170.49
			DBV[1] = -189.54
			DTH[1] = -167.57
			DBH[1] = -186.26
			#String 3
			DTV[2] = -170.39
			DBV[2] = -189.44
			DTH[2] = -167.27
			DBH[2] = -186.32
			#String 4
			DTV[3] = -170.67
			DBV[3] = -189.56
			DTH[3] = -167.72
			DBH[3] = -186.28
			#Pulsers
			DP[0] = -189.64
			DP[1] = -192.93
			DP[2] = -164.65
			DP[3] = -167.94
			#Fill the coordinates for all the detectors
			for i in range(4):
				station_coordinates[i][0] = (string[i][0], string[i][1], DTV[i])
				station_coordinates[i][1] = (string[i][0], string[i][1], DTH[i])
				station_coordinates[i][2] = (string[i][0], string[i][1], DBV[i])
				station_coordinates[i][3] = (string[i][0], string[i][1], DBH[i])
			station_coordinates[4][0] = (string[4][0], string[4][1], DP[0])
			station_coordinates[4][1] = (string[4][0], string[4][1], DP[1])
			station_coordinates[4][2] = (string[5][0], string[5][1], DP[2])
			station_coordinates[4][3] = (string[5][0], string[5][1], DP[3])
			return station_coordinates#, station_coordinates2
		#ARA03
		elif station == 3:
			#X,Y coordinates
			string[0] = [4.41, -9.39]
			string[1] = [10.69, 3.51]
			string[2] = [-2.01, 9.41]
			string[3] = [-8.10, -3.71]
			string[4] = [38.01, -16.40]
			string[5] = [17.94, 36.39]
			#Z Coordinates
			#String 1
			DTV[0] = -173.39
			DBV[0] = -192.45
			DTH[0] = -170.27
			DBH[0] = -189.20
			#String 2
			DTV[1] = -173.97
			DBV[1] = -192.70
			DTH[1] = -170.02
			DBH[1] = -189.74
			#String 3
			DTV[2] = -174.11
			DBV[2] = -192.67
			DTH[2] = -170.63
			DBH[2] = -189.71
			#String 4
			DTV[3] = -173.55
			DBV[3] = -192.60
			DTH[3] = -170.59
			DBH[3] = -189.48
			#Pulsers
			DP[0] = -194.90
			DP[1] = -198.18
			DP[2] = -184.73
			DP[3] = -188.01
			#Fill the coordinates for all the detectors
			for i in range(4):
				station_coordinates[i][0] = (string[i][0], string[i][1], DTV[i])
				station_coordinates[i][1] = (string[i][0], string[i][1], DTH[i])
				station_coordinates[i][2] = (string[i][0], string[i][1], DBV[i])
				station_coordinates[i][3] = (string[i][0], string[i][1], DBH[i])
			station_coordinates[4][0] = (string[4][0], string[4][1], DP[0])
			station_coordinates[4][1] = (string[4][0], string[4][1], DP[1])
			station_coordinates[4][2] = (string[5][0], string[5][1], DP[2])
			station_coordinates[4][3] = (string[5][0], string[5][1], DP[3])
			return station_coordinates#, station_coordinates2
		else:
			print 'Invalid station ID'
			return 0

	#Takes in the station number and returns keys and station information
	def get_station(self,station=2):
		return np.array([self.stations[0],self.stations[station-1]])
	
	#Returns the detector coordinates for a given string and station
	def get_string_coordinates(self, station=2, string=1, detector=0):
		return np.array([self.stations[station-1][string-1][detector][0], self.stations[station-1][string-1][detector][1], self.stations[station-1][string-1][detector][2]])
