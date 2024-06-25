plt.rc('axes',labelsize=14)
plt.rc('axes', axisbelow=True)

plt.rc('xtick',labelsize=14)
plt.rc('ytick',labelsize=14)
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
