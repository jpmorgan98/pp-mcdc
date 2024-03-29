import numpy as np
import os
import timeit
import time

N_list = np.logspace(5, 7, 3).astype(int)
runtimes = np.zeros(9)


for i in range( N_list.size ):
   print("Running {0} particles".format(N_list[i]))

   start = time.time()

   os.system("srun -n 36 python input.py"
        + " --mode=numba --N_particle=%i"%int(N_list[i])
        + " --output=output_%i"%int(N_list[i]))

   end = time.time()
   print(start-end)
   runtimes[i] = end-start

   print("Runtime: {0}".format( runtimes[i] ))
   print()

print(runtimes)

np.savez('mcdc_kobyashi_runtimes.npz', N_list = N_list, runtimes=runtimes)