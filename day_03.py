def calculate_priority(letter):
    if letter.islower():
        return ord(letter) - 96
    else:
        return ord(letter) - 38


def split_rucksack_into_comps(line):
    line_length = len(line)
    rucksack_length = int(line_length/2)
    return line[0:rucksack_length], line[rucksack_length:]

if __name__ == "__main__":
    # Get the input data
    with open("inputs/day_03.txt", "r") as f:
        file_data = f.read()

    # Part 1
    totals = []
    for line in file_data.split("\n"):
        first_comp, second_comp = split_rucksack_into_comps(line)
        common = set([x for x in first_comp if x in second_comp])
        totals += list(common)
    priorities = [calculate_priority(x) for x in totals]
    print(f"Answer to part 1: {sum(priorities)}")

    # Part 2
    with open("inputs/day_03.txt", "r") as f:
        file_data = f.read()
    split_lines = [line for line in file_data.split("\n")]
    iterations = int(len(split_lines) /3)

    start_index = 0
    finish_index = 3
    total_priority = 0
    for i in range(0, iterations):
        cache = []
        for line in split_lines[start_index:finish_index]:
            if not cache:
                cache = [x for x in line]
            else:
                cache = [x for x in line if x in cache]
        priority = calculate_priority(list(set(cache))[0])
        total_priority += priority
        start_index += 3
        finish_index += 3

    print(f"Answer to part 2: {total_priority}")
