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

default_cycler = (cycler(color=['r', 'g', 'b', 'y']) +
                  cycler(linestyle=['-', '--', ':', '-.']))

plt.rc('lines', linewidth=4)
custom_cycler = (cycler(color=['c', 'm', 'y', 'k']) +
                 cycler(lw=[1, 2, 3, 4]))

#plt.rc('axes', prop_cycle=default_cycler)
plt.rc('axes', prop_cycle=custom_cycler)

data_file  = "/Users/nneveu/github/hombom/data/2024_data_charge.txt"

# Number of PVs = 15
# 8 HOM BOM signals
# 1 Charge signal
# 6 BPM (3 x BPM and 3 y BPM)
cnames = ['Timestamp',
          'BPMS:L0B:0183:FW:X_SLOW','Status1', 
          'BPMS:L0B:0183:FW:Y_SLOW','Status2',
          'BPMS:HTR:120:FW:X_SLOW', 'Status3',
            'BPMS:HTR:120:FW:Y_SLOW', 'Status4',
            'BPMS:GUNB:925:FW:X_SLOW','Status5',
            'BPMS:GUNB:925:FW:Y_SLOW',	'Status6',
            'SCOP:AMRF:RF01:AI_MEAS1',	'Status7',
            'SCOP:AMRF:RF01:AI_MEAS2',	'Status8',
            'SCOP:AMRF:RF01:AI_MEAS3',	'Status9',
            'SCOP:AMRF:RF01:AI_MEAS4',	'Status10',
            'SCOP:AMRF:RF03:AI_MEAS1',	'Status11',
            'SCOP:AMRF:RF03:AI_MEAS2', 'Status12',
            'SCOP:AMRF:RF03:AI_MEAS3',	'Status13',	
            'SCOP:AMRF:RF03:AI_MEAS4',	'Status14',	
            'TORO:GUNB:360:CHRG',	'Status15',	'blah'
]
plot_names = ['Timestamp',
          'CM BPM X','Status1', 
          'CM BPM Y','Status2',
          'HTR BPM X', 'Status3',
            'HTR BPM Y', 'Status4',
            'GUN BPM X','Status5',
            'GUN BPM Y',	'Status6',
            'HOM C1',	'Status7',
            'HOM C2',	'Status8',
            'HOM C3',	'Status9',
            'HOM C4',	'Status10',
            'HOM C5',	'Status11',
            'HOM C6', 'Status12',
            'HOM C7',	'Status13',	
            'HOM C8',	'Status14',	
            'Charge',	'Status15',	'blah'
]
drops = np.arange(3, 46, 3)
#drops = [int(val) for val in drops]
#print(drops)
df = pd.read_csv(data_file, sep='\t', skiprows=100, header=None)#, names=cnames)
#print(list(df.columns.values))
#print(df.iloc[:,2])

new_df    = df[~df[2].str.contains('INVALID', na=False)]
new_names = list(new_df.columns.values) 
drop_df   = new_df.drop(df.columns[drops], axis=1)
#drop_df   = new_df.drop(df.columns[46], axis=1)
drop_df.columns = plot_names #cnames
drop_names = list(drop_df.columns.values)
#print(len(new_names))
#print(len(drop_names))
#print(len(cnames))
#print(list(new_df.columns.values))
#print(new_df.iloc[:,4])

charge = drop_df["Charge"]
hom1   = drop_df["HOM C1"]
hom2   = drop_df["HOM C2"]
hom3   = drop_df["HOM C3"]
hom4   = drop_df["HOM C4"]
hom5   = drop_df["HOM C5"]
hom6   = drop_df["HOM C6"]
hom7   = drop_df["HOM C7"]
hom8   = drop_df["HOM C8"]
bpm_gunx = drop_df['GUN BPM X']
bpm_guny = drop_df['GUN BPM Y']
bpm_cmx  = drop_df['CM BPM X']
bpm_cmy  = drop_df['CM BPM Y']
time = drop_df['Timestamp']

def get_timestamps(df, timestart, timestop):
    #index_start = df[df['Timestamp'].str.startswith(timestart)==True].index[0]
    #index_stop  = df[df['Timestamp'].str.startswith(timestop)==True].index[-1]
    #return pd.concat([df[index_start==True],df[index_stop==True]])
    mask = df['Timestamp'].str.startswith(timestart) | df['Timestamp'].str.startswith(timestop)
    #import pdb; pdb.set_trace()
    return  df[mask] #df[index_start:index_stop]

#Shorten data
df_short = get_timestamps(drop_df, '02/24/2024 16', '02/24/2024 20')
print(df_short)
# FJD HOM 1 signal vs. bpm
short_time = df_short['Timestamp']
short_gunbpmx = df_short['GUN BPM X']
short_gunbpmy = df_short['GUN BPM Y']
short_hom1 = df_short['HOM C1']
plt.plot(short_time, short_gunbpmx, 'x', label='Gun BPM x')
plt.plot(short_time, short_gunbpmy, '^', label='Gun BPM y')
plt.plot(short_time, short_hom1, '.', label='Gun BPM x')
plt.show()

#plt.plot(time, bpm_guny, 'kx', label='Gun BPM y', alpha=0.5)
#plt.plot(time, bpm_cmx, 'b.', label='CM BPM x')
#plt.plot(time, bpm_cmy, 'm^', label='CM BPM y', alpha=0.5)
#plt.plot(time, hom1, 'k--', label='HOM Cavity 1')
plt.ylabel('HOM Signal [arb.], BPM [mm]')
plt.xlabel('Time')
plt.legend(loc='best')
#plt.xlim(-5, 5)
#plt.ylim( -0.5, 0.0)
#plt.savefig('cav1_bpm_hom_all_data.png', dpi=200, bbox_inches='tight')
#plt.show()

# HOM 1 Signal vs. Charge plot
# Calculate the point density
""" xy = np.vstack([charge,hom1])
z = gaussian_kde(xy)(xy)
plt.scatter(charge, hom1, c=z, s=50, label='Cavity 1')
plt.ylabel('HOM Signal Cavity 1 [arb.]')
plt.xlabel('Charge [pC]')
#plt.legend(loc='best')
plt.xlim(5,200)
plt.ylim( -0.5, 0.0)
#plt.savefig('cav1_hom_charge_all_data.png', dpi=200, bbox_inches='tight')
#plt.show() """

""" # HOM 1 and 5 signal
plt.plot(charge, hom1, 'yo', label='Cavity 1')
plt.plot(charge, hom5, 'kx', label='Cavity 5', alpha=0.5)
plt.ylabel('HOM Signal [arb.]')
plt.xlabel('Charge [pC]')
plt.legend(loc='best')
plt.xlim(1,200)
plt.ylim( -0.5, 0.0)
plt.savefig('cav1_cav5_hom_charge_all_data.png', dpi=200, bbox_inches='tight')
#plt.show() """
 
""" # HOM all
plt.plot(charge, hom1, 'o', label='Cavity 1')
plt.plot(charge, hom2, 'o', label='Cavity 2')
plt.plot(charge, hom3, 'o', label='Cavity 3')
plt.plot(charge, hom4, 'o', label='Cavity 4')
plt.plot(charge, hom5, 'x', label='Cavity 5', alpha=0.5)
plt.plot(charge, hom6, 'x', label='Cavity 6')
plt.plot(charge, hom7, 'x', label='Cavity 7')
plt.plot(charge, hom8, 'x', label='Cavity 8')
plt.ylabel('HOM Signal [arb.]')
plt.xlabel('Charge [pC]')
plt.legend(loc='best')
plt.xlim(1,200)
plt.ylim( -0.5, 0.0)
#plt.savefig('cav1-8_hom_charge_all_data.png', dpi=200, bbox_inches='tight')
#plt.show()  """

