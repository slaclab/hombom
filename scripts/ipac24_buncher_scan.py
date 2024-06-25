import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib import cycler
from scipy.stats import gaussian_kde

plt.rc('axes',labelsize=24)
plt.rc('axes', axisbelow=True)

plt.rc('xtick',labelsize=18)
plt.rc('ytick',labelsize=18)
plt.rc('font', family='STIXGeneral')
plt.rc('mathtext', fontset='stix')
plt.rc('legend', fontsize='14')
plt.rc('lines', linewidth=4)


default_cycler = (cycler(color=['r', 'g', 'b', 'y']) +
                  cycler(linestyle=['solid', 'dotted', 'dashed', ':']))

custom_cycler = (cycler(color=['c', 'm', 'y', 'k']) +
                 cycler(lw=[2, 2, 2, 2]))

plt.rc('axes', prop_cycle=custom_cycler)

data_file  = "/Users/nneveu/github/hombom/data/2024_fjd_phase_scan.csv"
names = list(['Timestamp','GUN BPM X','GUN BPM Y','HOM C1'])
df = pd.read_csv(data_file, sep=',', skiprows=1, header=None, names=names)

# FJD HOM 1 signal vs. bpms
time = np.linspace(0,8,726) #df['Timestamp']
gunbpmx = df['GUN BPM X'].interpolate()
gunbpmy = df['GUN BPM Y'].interpolate()
hom1 = df['HOM C1'].interpolate()
# time[0]'2024/02/24 18:38:57.953'
# time[-1] '2024/02/24 18:46:12.315'
'''
fig, ax1 = plt.subplots()
color1 = '#40B0A6'
ax1.set_xlabel('Time (min)')
ax1.set_ylabel('GUN BPM [mm]', color=color1)
ax1.plot(time, gunbpmx, '-.', color=color1, label='Gun BPM x')
ax1.plot(time, gunbpmy, '--', color='k', label='Gun BPM y')
ax1.tick_params(axis='y', labelcolor=color1)
ax2 = ax1.twinx()

#import pdb; pdb.set_trace()
color2 = '#E1BE6A'
ax2.set_ylabel('HOM Signal Cavity 1 [arb.]', color=color2)  
#ax2.fill_between(time, hom1)
ax2.plot(time, np.array(hom1), '-', color=color2, label='HOM Cavity 1')
ax2.tick_params(axis='y', labelcolor=color2)
ax2.set_ylim(-0.5,0)
ax1.legend(loc='best')
#ax2.legend(loc='best')
fig.tight_layout() 
plt.show()
'''
start = 400
stop = 500
time_short = time[start:stop]
gunbpmx_short = gunbpmx[start:stop]
gunbpmy_short = gunbpmy[start:stop]
hom1_short = hom1[start:stop]

fig, ax1 = plt.subplots()
color1 = '#40B0A6'
ax1.set_xlabel('Time (min)')
ax1.set_ylabel('GUN BPM X [mm]', color=color1)
ax1.plot(time_short, gunbpmx_short, 'x-', color=color1, label='Gun BPM x')
#ax1.plot(time_short, gunbpmy_short, '--', color='k', label='Gun BPM y')
ax1.tick_params(axis='y', labelcolor=color1)
ax2 = ax1.twinx()

#import pdb; pdb.set_trace()
color2 = '#E1BE6A'
ax2.set_ylabel('HOM Signal Cavity 1 [arb.]', color=color2)  
#ax2.fill_between(time, hom1)
ax2.plot(time_short, hom1_short, 'o-', color=color2, label='HOM Cavity 1')
ax2.tick_params(axis='y', labelcolor=color2)
ax2.set_ylim(-0.5,0)
#ax1.legend(loc='best', prop={'size': 20})
#ax2.legend(loc='best')
fig.tight_layout() 
plt.show()

