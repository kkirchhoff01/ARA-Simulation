from matplotlib import pyplot as plt
import pylab
import sys

class Plot_Askaryan:
	def read_data(self, file_name=''):
		self.data = []
		with open(file_name, 'r') as f:
			temp = f.read().split('\n')
			#temp.remove('')
			for t in temp:
				if t == '' or t == '\n':
					pass
				else:
					self.data = self.data + t.split(' ')
		return self.data

	def plot_data(self, fname='', save=False, title='', name='', distance=1.0):
		self.read_data(fname)
		self.data = [float(d)/distance for d in self.data]
		if save == True:
			fig = plt.figure()
			ax = fig.gca()
			ax.plot(self.data)
			ax.set_xlim([8550, 8800])
			ax.set_xlabel('Time (ns)')
			ax.set_ylabel('V')
			ax.set_title(title)
			plt.savefig('Images/EM_Plots/' + name + '.png')
		else:
			fig, ax = plt.subplots(4,4)
			print self.data
			for i in range(4):
				for j in range(4):
					ax[i][j].plot(self.data[i][j])
			plt.xlim([8550, 8800])
			plt.show()

	def write_data(self, name=''):
		file_name = 'Images/EM_Dat_Files/' + name + '.dat'
		file_writer = open(file_name, 'w')
		for d in self.data:
			file_writer.write(str(d))
			file_writer.write('\n')
		file_writer.close()
