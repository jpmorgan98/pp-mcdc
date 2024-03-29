import numpy as np
import os
import timeit


N_list = np.logspace(5, 9, 9).astype(int)
runtimes = np.zeros(9).astype(float)

for i in range( N_list.size ):
   print("Running {0} particles",N_list[i])
   start = timeit.timeit()
   os.system("srun -n 36 python input.py"
        + " --mode=numba --N_particle=%i"%int(N_list[i])
        + " --output=output_%i"%int(N_list[i]))
   end = timeit.timeit()
   runtimes[i] = end-start
   print("Runtime: {0}", runtimes[i])
   print()

print(runtimes)