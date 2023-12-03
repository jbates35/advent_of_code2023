sum = 0

num_dict = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}

def check_if_key(compare_str):
    global num_dict
    for _ in range(3):
        if compare_str in num_dict:
            return num_dict[compare_str]
        compare_str = compare_str[:-1]
    else:
        return None

with open("data.txt", mode="r", encoding="utf-8") as f:
    for line in f:
        x = 0
        y = 0

        for i in range(0, len(line)):
            try:
                x = int(line[i])
            except Exception:
                pass
            else:
                break
            x = check_if_key(line[i:i+5])
            if x is not None:
                break

        for j in range(len(line), -1, -1):
            try:
                y = int(line[j])
            except Exception:
                pass
            else:
                break
            y = check_if_key(line[j:j+5])
            if y is not None:
                break
            
        sum += x*10 + y


print(sum) 

