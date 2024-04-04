import numpy as np
import matplotlib.pyplot as plt


N_particles = np.logspace(5, 9, 10).astype(int)
#N_particles = N_particles[:-2]


# OpenMC 36 Quartz cores with implicit capture
cpu_openmc = np.array([1.80948740e-01, 3.59284311e-01, 8.55737064e-01, 2.24981517e+00,
                       6.10727145e+00, 1.70394432e+01, 4.74983575e+01, 1.32280643e+02,
                       3.66327905e+02, 1.02254158e+03,]) 

# OpenMC 36 Quartz cores with out implicit capture
cpu_openmc_ic = np.array([4.79430673e-01, 1.19420164e+00, 3.22076232e+00, 8.74987371e+00,
                          2.44733171e+01, 6.85833251e+01, 1.89504849e+02, 5.30266883e+02,
                          1.48818073e+03, 4.12542630e+03]) 


# MCDC 36 Quartz cores with implicit capture, cached
# The last two particle counts where DNF even with a whole individual 12hr allocation on quartz (the max)
cpu_mcdc_ic_cached = np.array([2.30908818e+01, 3.52797744e+01, 7.68255820e+01, 1.92401531e+02, 
                          5.15599523e+02, 1.48727268e+03, 3.90907587e+03, 1.10168888e+04,
                          None, None])

# MCDC 36 Quartz cores without implicit capture, cached
cpu_mcdc_cached = np.array([11.40424776,    13.35105252,    21.37297511,    36.76940751,
                            84.33231568,   217.58568048,  589.87280846,  1642.11868,
                            4496.13040018, 12547.16239882]) 

cpu_mcdc_ic = np.array([1.62,    1.88,   2.60,   4.54,
                        10.03,    25.18,   1.18*60,  3.09*60,
                        None, None])
cpu_mcdc_ic[:-2] *=60

# MCDC 36 Quartz cores without implicit capture, not cached
cpu_mcdc = np.array([105.74024415,    99.98365736,   104.99810123,   122.85907364,
                    171.9013555,    317.06319618,   685.46320891,  1761.91955733,
                    4663.31377125, 12852.59791422])

cpu_copmile_times = np.array([59.07, 56.26, 56.05, 55.86, 56.03, 56.05, 56.49, 56.50, 56.62, 56.05])
# throwing out first compilation time, for compiler spinup 
cpu_avg_copmile_time = np.mean(cpu_copmile_times[1:])
cpu_compile_time = cpu_avg_copmile_time*np.ones(10)



gpu_copmile_times = np.array([59.07, 56.26, 56.05, 55.86, 56.03, 56.05, 56.49, 56.50, 56.62, 56.05])
# throwing out first compilation time, for compiler spinup 
gpu_avg_copmile_time = np.mean(gpu_copmile_times[1:])
gpu_compile_time = gpu_avg_copmile_time*np.ones(10)

# MCDC V100 Lassen GPU data with implicit capture, not cached
N_particles_gpu = N_particles
gpu_mcdc_ic = np.array([200.6173296,   198.0095706,   196.53112364,  201.75874662,
                          209.82980871, 238.05999756,  318.33002305,  529.6794126,
                          1130.28965092, 2788.41011333])

# MCDC V100 Lassen GPU data with out implicit capture, not cached
N_particles_gpu = N_particles
gpu_mcdc = np.array([200.31790972, 196.38998604, 196.0286355, 196.46965742,
                          197.45999694, 200.821872, 212.55772901, 238.27978778,
                          316.05001473, 529.82965326])


# Really just the Numba from Pyhton to PTX time, not the GPU total compilation time
print('Average GPU compile time ', gpu_avg_copmile_time)
#print('Average CPU compile time ', cpu_avg_copmile_time)

print('OpenMC v MC/DC cached speedup IC ', cpu_mcdc_ic_cached[-3]/cpu_openmc_ic[-3])
print('OpenMC v MC/DC ceched speedup Analog ', cpu_mcdc_cached[-1]/cpu_openmc[-1])

print('GPU v CPU speedup IC ', cpu_mcdc_ic_cached[-3]/gpu_mcdc_ic[-3])
print('GPU v CPU speedup Analog ', cpu_mcdc_cached[-1]/gpu_mcdc[-1])



#openMC vs MC/DC with and without IC
plt.figure(1)
plt.plot(N_particles, cpu_openmc, '-*r', label='OpenMC')
plt.plot(N_particles, cpu_openmc_ic, '--^r', label='OpenMC (IC)')
plt.plot(N_particles, cpu_mcdc_cached, '-^k', label='MC/DC')
plt.plot(N_particles, cpu_mcdc_ic_cached, '--^k', label='MCDC (IC)')
plt.yscale('log')
plt.xscale('log')
plt.grid()
plt.legend()
plt.xlabel("N_particle")
plt.ylabel("Wall Clock Runtime [s]")
plt.savefig('code_comparisons.png')

# MC/DC GPU v MC/DC CPU (36 cores) #with and without compile time
plt.figure(2)
plt.plot(N_particles, cpu_mcdc, '-*k', label='CPU')
plt.plot(N_particles, cpu_mcdc_ic, '--*k', label='CPU (IC)')
plt.plot(N_particles, gpu_mcdc, '-^g', label='GPU')
plt.plot(N_particles, gpu_mcdc_ic, '--^g', label='GPU (IC)')
#plt.plot(N_particles, gpu_compile_time)
plt.yscale('log')
plt.xscale('log')
plt.grid()
plt.legend()
plt.xlabel("N_particle")
plt.ylabel("Wall Clock Runtime [s]")
plt.savefig('mcdc_comparisons.png')