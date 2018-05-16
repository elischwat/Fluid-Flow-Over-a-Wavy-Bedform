import numpy as np
from matplotlib import pyplot as plt

def plotWavyBedform():
	#Set up our figure to contain 3 subplots
	fig, axs = plt.subplots(3, 1, sharex=True, figsize=(12,8))
	# Remove horizontal space between axes of the 3 subplots
	fig.subplots_adjust(hspace=.1)
	# Plot streambed waveform:
	plt.subplot2grid((5,3), (3,0), colspan=3, rowspan=2)
	# plot bedform
	plt.plot(x, bedform, label='Stream Bed')
	# make it pretty...
	plt.xlim(0,lamb)
	ax = plt.gca(); ax.spines['right'].set_visible(False); ax.spines['top'].set_visible(False)
	plt.annotate('$\eta$', xy=(lamb,0), fontsize=22)
	plt.xlabel('Streamwise Distance (m)')
	plt.ylabel('Bedform \n Elevation (m)')

	# Plot fluid velocity waveform:
	plt.subplot2grid((5,3), (0,0), colspan=3, rowspan=1)
	plt.plot(x, velocity + U)
	plt.xlim(0,lamb)
	ax = plt.gca(); ax.axes.get_xaxis().set_visible(False)
	ax.spines['right'].set_visible(False); ax.spines['top'].set_visible(False); ax.spines['bottom'].set_visible(False)
	plt.annotate('$u$', xy=(lamb,1.0), fontsize=22)
	plt.ylabel('Velocity (m/s)')

	# Plot fluid surface waveform:
	plt.subplot2grid((5,3), (1,0), colspan=3, rowspan=2)
	plt.plot(x, surface + H)
	plt.xlim(0,lamb)
	ax = plt.gca()
	ax.axes.get_xaxis().set_visible(False)
	ax.spines['bottom'].set_visible(False); ax.spines['right'].set_visible(False); ax.spines['top'].set_visible(False)
	plt.annotate('$\zeta$', xy=(lamb,1.0), fontsize=22)
	plt.ylabel('Water Surface \n Elevation (m)')
	plt.show()