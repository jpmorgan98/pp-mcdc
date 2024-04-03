import numpy as np
import matplotlib.pyplot as plt


N_particles = np.logspace(5, 9, 10).astype(int)
#N_particles = N_particles[:-2]

#without implicit capture
cpu_mcdc_data = np.array([15.96044922,    13.35105252,    21.37297511,    36.76940751,
                            84.33231568,   217.58568048,  589.87280846,  1642.11868,
                            4496.13040018, 12547.16239882]) 

# Data from with implicit capture
N_particles_gpu = N_particles
gpu_mcdc_data = np.array([200.6173296,   198.0095706,   196.53112364,  201.75874662,
                          209.82980871, 238.05999756,  318.33002305,  529.6794126,
                          1130.28965092, 2788.41011333])

plt.figure()
plt.plot(N_particles, cpu_mcdc_data, '-*r', label='36 Core CPU')
plt.plot(N_particles_gpu, gpu_mcdc_data, '-^k', label='Tesla V100')
plt.yscale('log')
plt.xscale('log')
plt.grid()
plt.legend()
plt.xlabel("N_particle [s]")
plt.ylabel("Wall Clock Runtime [s]")
plt.show()
