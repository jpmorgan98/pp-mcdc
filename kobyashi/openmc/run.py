import os, h5py
import numpy as np

N_list = np.logspace(5, 9, 10).astype(int)
runtimes = np.zeros(10)

for i, N in enumerate(N_list):
    os.system('python build_xml.py %i'%N)

    os.system('srun -n 36 openmc')
    with h5py.File('statepoint.10.h5', "r") as f:
        runtimes[i] = f['runtime/simulation'][()]

np.savez('openmc_kobyashi_runtimes.npz', N_list=N_list, runtimes=runtimes)
