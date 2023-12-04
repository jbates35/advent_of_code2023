import re

power = 0
sum = 0

MAX_COUNTS = {"red": 12, "green": 13, "blue": 14}

with open("data1.txt", "r") as f:
    for line in f:
        words = re.split(";|:", line)
        words = list(filter(None, words))

        game_id = int(words[0].split()[1])

        words = words[1:]

        is_valid = True

        min_cubes_possible = {"red": 0, "green": 0, "blue": 0}

        for word in words:
            vals = re.split(",| |\n", word)
            vals = list(filter(None, vals))

            for i in range(0, len(vals), 2):
                # part 2
                if int(vals[i]) > min_cubes_possible[vals[i + 1]]:
                    min_cubes_possible[vals[i + 1]] = int(vals[i])

                # Part 1
                if int(vals[i]) > MAX_COUNTS[vals[i + 1]]:
                    is_valid = False

        mcp = min_cubes_possible
        power += mcp["red"] * mcp["green"] * mcp["blue"]

        if is_valid:
            sum += game_id

print(power)
print(sum)
