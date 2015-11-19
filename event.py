#from Askaryan import Askaryan
from station_geometry import station_geometry
import numpy as np
import sys
import random
import math

class event:
	def __init__(self):
		self.coordinates = self.station_coordinates()
		#self.askaryan_data = self.create_event(e,t)
	
	#Gets the coordinates of each detector (except calibration strings)
	def station_coordinates(self):
		station = station_geometry()
		coords = np.empty((4,4,3), dtype=float)
		for i in range(4):
			#loops through antennas
			for j in range(4):
				coords[i][j][0] = station.get_string_coordinates(2,i+1, j)[0]
				coords[i][j][1] = station.get_string_coordinates(2,i+1, j)[1]
				coords[i][j][2] = station.get_string_coordinates(2,i+1, j)[2]
		return coords

	#Creates an Askaryan event (not really used)
	'''
	def create_event(self, energy, theta):
		h = Askaryan()
		freqs = []
		fmax = 10.0
		df = 2.0*10**(-3)
		i = df
		while i < fmax:
			freqs.append(i)
			i += df
		h.setAskFreq(freqs)
		h.standardInitialize()
		h.emShower(energy)
		h.setAskTheta(theta*np.pi/180.0)
		return h
	'''	
	#Creates a random event vertex and direction
	#Then finds the angle of the detector relative to the direction
	#Returns the vertex point, direction, angle and distance of the detectors
	def create_vertex(self, r=1.0):
		#Generate random 3D vertex point
		#Random values taken from maximum neutrino detection distance
		vertex_point = (random.uniform(-3000,3000), random.uniform(-3000,3000), random.uniform(-4000,0))
		print vertex_point
		#Generate random 3D unit direction vector
		unit_direction_vector = (random.uniform(-1,1), random.uniform(-1,1), random.uniform(-1,1))
		#Direction vector scaled for plotting
		direction_vector = (vertex_point[0]+(500.0*unit_direction_vector[0]), vertex_point[1]+(500.0*unit_direction_vector[1]), vertex_point[2]+(500.0*unit_direction_vector[2]))
		print direction_vector
		distances = self.get_R(vertex_point)
		off_cone_angle = np.empty((4,4), dtype=float)
		#Loops through all detectors and calculates the angle relative to the direction
		for i in range(4):
			for j in range(4):
				#Angle from the cone direction
				detector_vertex_direction = (self.coordinates[i][j][0]-vertex_point[0], self.coordinates[i][j][1]-vertex_point[1], self.coordinates[i][j][2]-vertex_point[2])
				#Angle calculated with dot product by solving for theta
				off_cone_angle[i][j] = math.degrees(math.acos(np.dot(detector_vertex_direction, unit_direction_vector)/(np.linalg.norm(detector_vertex_direction)*np.linalg.norm(unit_direction_vector))))
		return vertex_point, direction_vector, off_cone_angle, distances
	
	#Get distance of detector from event	
	def get_R(self, event_location=np.zeros(3, dtype=float)):
		detector_distances = np.empty((4,4), dtype=float)
		for i in range(4):
			for j in range(4):
				detector_distances[i][j] = np.linalg.norm(self.coordinates[i][j] - event_location)
		
		return detector_distances

	#Not finished
	'''
	def get_energy(self, ask, location=np.zeros(3), energy=2000000.0, theta=56.0):
		ask = self.create_event(energy, theta)
		eTheta = ask.E_t()
		#Need dynamic R in MC code to set
		R = self.get_R(location)
		#e_total = 
	'''
