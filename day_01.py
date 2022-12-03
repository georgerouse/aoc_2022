if __name__ == '__main__':
    # Get the input data
    with open('inputs/day_01.txt') as f:
        file_data = f.read()

    file_totals = []
    elf_total = 0
    for line in file_data.split('\n'):
        if line != '':
            value = int(line)
            elf_total += value
        else:
            file_totals.append(elf_total)
            elf_total = 0

    print(f"Answer to part 1: {max(file_totals)}")

    top_3 = sorted(file_totals, reverse=True)[:3]
    print(f"Answer to part 2: {sum(top_3)}")
