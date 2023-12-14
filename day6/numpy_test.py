import numpy as np
from random import randint
import time


timer_start = time.time()
time_var = np.zeros(1, dtype="int8")
for _ in range(100000):
    time_var = np.append(time_var, [randint(0, 255)])
timer_end = time.time()
print(f"Timer for python with numpy append, {-timer_start + timer_end}")

timer_start = time.time()
time_var = np.zeros(1, dtype="int8")
for _ in range(100000):
    time_var = np.concatenate((time_var, [randint(0, 255)]))
timer_end = time.time()
print(f"Timer for python with numpy concatenate, {-timer_start + timer_end}")

timer_start = time.time()

time_var2 = [1]
for _ in range(100000):
    time_var2.append(randint(0, 1000))
time_var3 = np.array(time_var2)

timer_end = time.time()
print(f"Timer for python without numpy, {-timer_start + timer_end}")

timer_start = time.time()

time_var4 = np.zeros(1000)
np_length = 0
np_size = 1000

for _ in range(100000):
    if np_length == np_size:
        np_size *= 2
        time_var4 = np.resize(time_var4, np_size)
    time_var2.append(randint(0, 1000))
time_var3 = np.array(time_var2)

timer_end = time.time()
print(f"Timer for python with numpy while resizing, {-timer_start + timer_end}")
