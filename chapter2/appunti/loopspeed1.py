import time
import random
from math import exp, sqrt
start_time = time.time()
S0 = 100
r = 0.05
T = 1.0
sigma = 0.2

value = []

for _ in range(10000000):
    ST = S0 * exp((r - 0.5 * sigma ** 2) * T + sigma * random.gauss(0,1) * sqrt(T))
    value.append(ST)

print("--- %s seconds ---" % (time.time() - start_time))

