import numpy as np
import matplotlib.pyplot as plt


N_particles = np.logspace(5, 9, 10).astype(int)
N_particles = N_particles[:-2]

cpu_mcdc_data = np.array([2.30908818e+01, 3.52797744e+01, 7.68255820e+01, 1.92401531e+02, 5.15599523e+02, 1.48727268e+03, 3.90907587e+03, 1.10168888e+04]) 

# Data from braxtons doc
N_particles_gpu = np.array([1e4, 1e5, 1e6, 1e7, 1e8]).astype(int)
gpu_mcdc_data = np.array([1.42, 1.43, 1.46, 1.76, 5.01])
gpu_mcdc_data *= 60


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
