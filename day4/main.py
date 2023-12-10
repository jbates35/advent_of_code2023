import re


def winning_cards(line):
    line_sum = 0

    for win in line["winners"]:
        for num in line["numbers"]:
            if win == num:
                line_sum += 1

    return line_sum


total_sum = 0
games = list()

with open("data.txt", "r", encoding="utf-8") as f:
    for line in f:
        sections = re.split("\\||:", line)
        numbers = [section.split() for section in sections]

        win_nums = tuple(int(number) for number in numbers[1])
        compare_nums = tuple(int(number) for number in numbers[2])
        games.append({"winners": win_nums, "numbers": compare_nums})

copies = [1] * len(games)

for i, game in enumerate(games):
    for cnt in range(copies[i]):
        games_to_check = winning_cards(game)

        for j in range(i + 1, i + games_to_check + 1):
            if j < len(games):
                copies[j] += 1

print(sum(copies))
