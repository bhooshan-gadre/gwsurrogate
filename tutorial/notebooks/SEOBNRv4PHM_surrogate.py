import gwsurrogate
import pylab as plt

precessing_opts = {
                                'init_orbphase': 0,
                                'init_quat': [1,0,0,0],
                                'return_dynamics': True
                                }

sur = gwsurrogate.LoadSurrogate('../test_gwsurrogate/surr_data/SEOBNRv4PHMSur.h5')

q = 14           # mass ratio, mA/mB >= 1.0
chiA = [-0.2, 0.4, 0.1]         # Dimensionless spin of heavier BH
chiB = [-0.5, 0.2, -0.4]        # Dimensionless of lighter BH
dt = 0.1                        # timestep size, Units of total mass M
f_low = 0                # initial frequency, f_low=0 returns the full surrogate

t, h, dyn = sur(q, chiA, chiB, dt=dt, f_low=f_low, ellMax=5, precessing_opts=precessing_opts)

plt.plot(t, h(2, -2))
plt.plot(t, h[(2, -2)])
plt.show()
