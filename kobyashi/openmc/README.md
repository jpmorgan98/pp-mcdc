All I need is time elapsed to run
```
N_list = np.logspace(5, 9, 10).astype(int)
```

If you could save the results in an `.npz` file that would be ideal which would look something like
```
np.savez('openmc_kobyashi_runtimes.npz', N_list = N_list, runtimes=runtimes)
```