from dataclasses import dataclass
from os import walk
from pprint import pprint


@dataclass
class NumPT:
    x: int = 0
    y: int = 0
    width: int = 0
    num: int = 0


@dataclass
class SymPT:
    x: int = 0
    y: int = 0


str_list = []
mat_list = []
num_list = []
sym_list = []
sum_list = []
star_list = []

with open("data.txt", "r", encoding="utf-8") as f:
    for line in f:
        str_list.append(line)
        mat_list.append(list(line))
        sym_list.append([])


for i, row in enumerate(mat_list):
    num = 0
    num_width = 0
    for j in range(len(row) - 1, -1, -1):
        symbol = row[j]
        add_int = False
        try:
            temp = int(symbol)
            num += temp * 10**num_width
            num_width += 1
            if j == 0:
                num_list.append(NumPT(x=j, y=i, width=num_width, num=num))
        except Exception:
            add_int = True
        else:
            continue

        if num_width > 0 and add_int:
            num_list.append(NumPT(x=j + 1, y=i, width=num_width, num=num))
            num_width = 0
            num = 0
        if symbol == "." or symbol == " " or symbol == "\n":
            continue
        if symbol == "*":
            star_list.append(SymPT(x=j, y=i))
        if add_int:
            sym_list[i].append(SymPT(x=j, y=i))

# part2
mult_sum = 0
for star_obj in star_list:
    alt_num_list = list()
    for num_obj in num_list:
        if (
            -1 <= num_obj.y - star_obj.y <= 1
            and num_obj.x - 1 <= star_obj.x < num_obj.x + num_obj.width + 1
        ):
            alt_num_list.append(num_obj)
    # print(star_obj)
    if not len(alt_num_list) == 2:
        continue
    mult_sum += alt_num_list[0].num * alt_num_list[1].num
print(mult_sum)

# part1
for num_obj in num_list:
    touching = False
    if num_obj.y > 0:
        for sym_obj in sym_list[num_obj.y - 1]:
            if num_obj.x - 1 <= sym_obj.x < num_obj.x + num_obj.width + 1:
                touching = True
                break
    if not touching and num_obj.y < len(sym_list) - 1:
        for sym_obj in sym_list[num_obj.y + 1]:
            if num_obj.x - 1 <= sym_obj.x < num_obj.x + num_obj.width + 1:
                touching = True
                break
    if not touching:
        for sym_obj in sym_list[num_obj.y]:
            if num_obj.x - 1 <= sym_obj.x < num_obj.x + num_obj.width + 1:
                touching = True
                break
    if touching:
        sum_list.append(num_obj)
    # else:
    #     print(num_obj.num)

# pprint(sum_list)
print(sum([x.num for x in sum_list]))
