import numpy as np
import matplotlib.pyplot as plt


N_particles = np.logspace(5, 9, 10).astype(int)
#N_particles = N_particles[:-2]


# OpenMC 36 Quartz cores with implicit capture
cpu_openmc = np.array([15.96044922,    13.35105252,    21.37297511,    36.76940751,
                            84.33231568,   217.58568048,  589.87280846,  1642.11868,
                            4496.13040018, 12547.16239882]) 

# OpenMC 36 Quartz cores with out implicit capture
cpu_openmc_ic = np.array([15.96044922,    13.35105252,    21.37297511,    36.76940751,
                            84.33231568,   217.58568048,  589.87280846,  1642.11868,
                            4496.13040018, 12547.16239882]) 




# MCDC 36 Quartz cores with implicit capture, cached
# The last two particle counts where DNF even with a whole individual 12hr allocation on quartz (the max)
cpu_mcdc_ic_cached = np.array([2.30908818e+01, 3.52797744e+01, 7.68255820e+01, 1.92401531e+02, 
                          5.15599523e+02, 1.48727268e+03, 3.90907587e+03, 1.10168888e+04,
                          None, None])

# MCDC 36 Quartz cores without implicit capture, cached
cpu_mcdc_cached = np.array([15.96044922,    13.35105252,    21.37297511,    36.76940751,
                            84.33231568,   217.58568048,  589.87280846,  1642.11868,
                            4496.13040018, 12547.16239882]) 

# MCDC 36 Quartz cores without implicit capture, not cached
cpu_mcdc = np.array([15.96044922,    13.35105252,    21.37297511,    36.76940751,
                            84.33231568,   217.58568048,  589.87280846,  1642.11868,
                            4496.13040018, 12547.16239882]) 

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
plt.plot(N_particles, cpu_mcdc, '-*r', label='CPU')
plt.plot(N_particles, cpu_mcdc_ic_cached, '--*r', label='CPU (IC)')
plt.plot(N_particles, gpu_mcdc, '-^k', label='GPU')
plt.plot(N_particles, gpu_mcdc_ic, '--^k', label='GPU (IC)')
plt.yscale('log')
plt.xscale('log')
plt.grid()
plt.legend()
plt.xlabel("N_particle")
plt.ylabel("Wall Clock Runtime [s]")
plt.savefig('mcdc_comparisons.png')