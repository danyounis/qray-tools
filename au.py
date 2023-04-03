import scipy.constants as mks

'''Hartree atomic units'''
a0 = mks.hbar/(mks.m_e*mks.c*mks.alpha) # Bohr radius (m)
c = 1.0/mks.alpha # speed of light (a.u.)
E = (mks.alpha**2)*mks.m_e*(mks.c**2) # 2*Rydberg energy (J)
t = mks.hbar/E # time (s)
F = E/mks.e/a0 # field strength (V/m)
I = 0.5*mks.c*mks.epsilon_0*(F**2) # intensity (W/m2)

units = {
'a0':'m',
'c':'a.u.',
'E':'J',
't':'s',
'F':'V/m',
'I':'W/m2'
};
