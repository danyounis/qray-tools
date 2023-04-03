import numpy as np
import matplotlib.pyplot as plt

'''inputs'''
omg0 = 0.4 # frequency (a.u.)
Tp = 250.0 # total pulse duration (a.u.)
CEP = np.pi/2 # carrier-envelope phase

'''definitions'''
g = lambda t: np.sin(np.pi*t/Tp)
f = lambda t: g(t)*np.sin(omg0*t + CEP)

t = np.linspace(0.0, Tp, int(1e+3))

plt.plot(t, g(t), '--k')
plt.plot(t, f(t), '-k')
plt.xlabel('Time (a.u.)')
plt.ylabel('Amplitude')
plt.show()
