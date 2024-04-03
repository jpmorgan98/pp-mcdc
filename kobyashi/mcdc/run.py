import numpy as np
import os
import timeit
import time

N_list = np.logspace(5, 9, 10).astype(int)
runtimes = np.zeros(10)
#N_list = N_list[-2:]

print(N_list)

for i in range( N_list.size ):
   print("Running {0} particles".format(N_list[i]))

   start = time.time()

   os.system("srun -n 36 python input.py"
        + " --no-progress-bar --mode=numba --target=gpu --N_particle=%i"%int(N_list[i])
        + " --output=output_%i"%int(N_list[i]))

   end = time.time()
   print(start-end)
   runtimes[i] = end-start

   print("Runtime: {0}".format( runtimes[i] ))
   print()

print(runtimes)
print(N_list)

np.savez('mcdc_gpu_kobyashi_runtimes.npz', N_list = N_list, runtimes=runtimes)
