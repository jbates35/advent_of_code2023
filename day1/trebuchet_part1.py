sum = 0

with open("data.txt", mode="r", encoding="utf-8") as f:
    for line in f:
        for i in range(0, len(line)):
            try:
                i = int(line[i])
            except:
                continue
            break
        for j in range(len(line), -1, -1):
            try:
                j = int(line[j])
            except:
                continue
            break
        sum += i*10 + j

print(sum) 
