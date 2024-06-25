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

data_file  = "/Users/nneveu/github/hombom/data/homs_only_april.csv"
names = list(['Timestamp','SCOP:AMRF:RF01:AI_MEAS1','SCOP:AMRF:RF03:AI_MEAS4',
              'SCOP:AMRF:RF03:AI_MEAS42','SCOP:AMRF:RF03:AI_MEAS1',
              'SCOP:AMRF:RF01:AI_MEAS4','SCOP:AMRF:RF01:AI_MEAS2',
              'SCOP:AMRF:RF01:AI_MEAS3','SCOP:AMRF:RF03:AI_MEAS2',
              'SCOP:AMRF:RF03:AI_MEAS3'])
df = pd.read_csv(data_file, sep=',', skiprows=1, header=None, names=names)

data_file2  = "/Users/nneveu/github/hombom/data/cavity1_phase_scan.csv"
names2 = list(['Timestamp','ACCL:L0B:0110:PDES','blah'])
df2 = pd.read_csv(data_file2, sep=',', skiprows=1, header=None, names=names2)
time2 = np.linspace(25,34,63) #df['Timestamp']
phase = df2['ACCL:L0B:0110:PDES'].interpolate()

# HOM 1 signal vs. phase 
time = np.linspace(6,27,2995) #df['Timestamp']
hom1 = df['SCOP:AMRF:RF01:AI_MEAS1'].interpolate()
hom2 = df['SCOP:AMRF:RF01:AI_MEAS2'].interpolate()
hom3 = df['SCOP:AMRF:RF01:AI_MEAS3'].interpolate()
hom4 = df['SCOP:AMRF:RF01:AI_MEAS4'].interpolate() 
# time[0]'2024/02/24 18:38:57.953'
# time[-1] '2024/02/24 18:46:12.315'

start = 2500
stop = -1
time_short = time[start:stop]
hom1_short = hom1[start:stop]
hom2_short = hom2[start:stop]
hom3_short = hom3[start:stop]
print(time_short)
fig, ax1 = plt.subplots()
color1 = '#40B0A6'
ax1.set_xlabel('Time (min)')
ax1.set_ylabel('Phase [deg.]', color=color1)
ax1.plot(time2, phase, 'x-', color=color1, label='HOM Cavity 1')
ax1.tick_params(axis='y', labelcolor=color1)
ax2 = ax1.twinx()

#import pdb; pdb.set_trace()
color2 = '#E1BE6A'
ax2.set_ylabel('HOM Signal Cavity 1 [arb.]', color=color2)  
#ax2.fill_between(time, hom1)
ax2.plot(time_short, hom1_short, 'x-', color=color1, label='HOM Cavity 1')
ax2.plot(time_short, hom2_short, 'o-', color=color2, label='HOM Cavity 2')
ax2.tick_params(axis='y', labelcolor=color2)
ax2.set_ylim(-0.5,0)
#ax1.legend(loc='best', prop={'size': 20})
#ax2.legend(loc='best')
fig.tight_layout() 
plt.show()

