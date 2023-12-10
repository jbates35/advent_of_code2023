import re
import pprint
from dataclasses import dataclass


@dataclass
class Converter:
    conv_to: int = 0
    conv_from: int = 0
    width: int = 0

    def convert(self, num):
        if self.conv_from <= num < self.conv_from + self.width:
            return num + (self.conv_to - self.conv_from), True
        else:
            return num, False


file_lines = list()
with open("data.txt", "r", encoding="utf-8") as f:
    for line in f:
        line = line.split("\n")
        file_lines.append(line[0])

temp_seeds = list()
seeds = list()
seeds_info = list()
conversion_maps = dict()

new_key = ""
conv_list = list()


for line in file_lines:
    if "seeds" in line:
        vals = re.split("\\'| ", line)
        for val in vals:
            try:
                x = int(val)
                temp_seeds.append(x)
            except Exception:
                pass
    elif "map" in line:
        vals = line.split()
        new_key = vals[0]
    elif line == "" and len(conv_list) > 0:
        conversion_maps[new_key] = conv_list.copy()
        conv_list.clear()
    else:
        vals = line.split()
        try:
            conv_end = int(vals[0])
            conv_start = int(vals[1])
            width = int(vals[2])
            conv_list.append(Converter(conv_end, conv_start, width))
        except Exception:
            continue

for i in range(0, len(temp_seeds), 2):
    for j in range(temp_seeds[i], temp_seeds[i + 1] + temp_seeds[i]):
        seeds.append(j)
conversion_maps[new_key] = conv_list.copy()

for i, _ in enumerate(seeds):
    for key, converter_list in conversion_maps.items():
        for converter in converter_list:
            seeds[i], converted = converter.convert(seeds[i])
            if converted:
                break

print(min(seeds))
# pprint.pprint(conversion_maps)
# pprint.pprint(file_lines)
