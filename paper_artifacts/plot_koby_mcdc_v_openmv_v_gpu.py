import numpy as np
import matplotlib.pyplot as plt


N_particles = np.array([N_list = np.logspace(5, 9, 10).astype(int)])
cpu_mcdc_data = np.array([2.30908818e+01, 3.52797744e+01, 7.68255820e+01, 1.92401531e+02, 5.15599523e+02, 1.48727268e+03, 3.90907587e+03, 1.10168888e+04]) 

N_particles_gpu = np.array([1e4, 1e5, 1e6, 1e7, 1e8]).astype(int)

gpu_mcdc_data = np.array([])
