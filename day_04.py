def expand_to_sets(range_str):
    start = int(range_str.split('-')[0])
    end = int(range_str.split('-')[1])
    return set([x for x in range(start, end+1)])

if __name__ == "__main__":
    # Get the input data
    with open("inputs/day_04.txt", "r") as f:
        file_data = f.read()
    overlap_count = 0
    any_overlap_count = 0
    for line in file_data.split("\n"):
        elf_1, elf_2 = line.split(',')
        elf_1 = expand_to_sets(elf_1)
        elf_2 = expand_to_sets(elf_2)
    
        if elf_1.issubset(elf_2) or elf_2.issubset(elf_1):
            overlap_count += 1
        
        if elf_1.intersection(elf_2) or elf_2.intersection(elf_1):
            any_overlap_count += 1
    
    print(f"Answer to part 1: {overlap_count}")
    print(f"Answer to part 1: {any_overlap_count}")        
