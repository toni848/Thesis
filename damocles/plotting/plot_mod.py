import numpy as np 
import matplotlib.pyplot as pl

wave,vel,flux  = np.loadtxt('output/output.out', skiprows=0,usecols = (0,1,2), unpack = True)

fig = pl.figure()
pl.xlabel('velocity (km/s)')
pl.ylabel('Flux')
pl.title('halpha')
#pl.ylim(1, 300)
#pl.xscale('log')
pl.plot(vel, flux,'b')
pl.axvline(x=-3800,color='black')
pl.axvline(x=3800,color='black')
#pl.plot(wave_dat,flux_dat,'r')
#pl.plot(x,y)
pl.xlim([-10000,10000])
#pl.savefig('line.eps')
pl.show()