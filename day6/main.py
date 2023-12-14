import re
import math
import time

dataset = []

timer = time.time()

with open("data.txt", "r", encoding="utf-8") as f:
    for line in f:
        dataline = ""

        for data in line.strip().split():
            try:
                x = int(data)
                dataline += str(x)
            except Exception:
                continue

        dataset.append([int(dataline)])

total_nums = []


for i in range(len(dataset[0])):
    t = dataset[0][i]
    d = dataset[1][i]

    x1 = math.ceil((t + math.sqrt(t * t - 4 * d)) / 2)
    x2 = math.floor((t - math.sqrt(t * t - 4 * d)) / 2)

    total_nums.append(x1 - x2 - 1)

print(f"time for algorithm: {time.time() - timer}")
print(dataset)
print(total_nums)
print(math.prod(total_nums))
