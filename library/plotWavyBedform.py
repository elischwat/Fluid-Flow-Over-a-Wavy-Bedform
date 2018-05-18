import numpy as np
from matplotlib import pyplot as plt

#Parameters: n0, lamb, U, g, H, gamm, x: bed waveform 
#    amplitude, bed waveform wavelength, average 
#    streamwise velocity, gravitational acceleration, 
#    average fluid depth, friction coefficient, 
#    x-domain
#returns: 3 waveforms in the following order: stream bed,
#    fluid surface height, depth-averaged streamwise
#    velocity.
def getPlots(n0, lamb, U, g, H, gamm, x):
    alpha = gamm/H
    beta = g*H/U**2
    omega = 2*np.pi/lamb
    u0 = (U/H)*n0*beta*omega/np.sqrt(9*alpha**2 + omega**2*(1-beta)**2)
    z0 = n0*(9*alpha**2 + omega**2)/np.sqrt(9*alpha**2 + omega**2*(1-beta)**2)
    phi_u = -np.pi/2 - np.arctan(omega*(1-beta)/(3*alpha))
    phi_z = np.arctan(omega/(3*alpha)) - np.arctan(omega*(1-beta)/(3*alpha))    
    n_ = n0*np.cos(omega*x)
    u_ = u0*np.cos(omega*x + phi_u)
    z_ = z0*np.cos(omega*x + phi_z)
    return(n_, z_, u_)

def plotWavyBedform(eta0, lamb, U, g, H, gamma, x):
	bedform, surface, velocity = getPlots(eta0, lamb, U, g, H, gamma, x)

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