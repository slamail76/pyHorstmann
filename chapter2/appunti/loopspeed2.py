import time
import numpy as np
start_time = time.time()
S0 = 100
r = 0.05
T = 1.0
sigma = 0.2

ST = S0 * np.exp((r - 0.5 * sigma ** 2) * T + sigma * np.random.standard_normal(10000000) * np.sqrt(T))
np.random.sta
#print(ST)


print("--- %s seconds ---" % (time.time() - start_time))