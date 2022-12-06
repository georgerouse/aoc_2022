def determine_start_index(file_data, marker_size=4):
    string_list = [x for x in file_data]
    for i in range(0, len(string_list) - marker_size):
        if (len(set(string_list[i:i+marker_size])) == len(string_list[i:i+marker_size]) and (len(string_list[i:i+marker_size]) == marker_size)):
            return i + marker_size
    

if __name__ == "__main__":
    # Get the input data
    with open("inputs/day_06.txt", "r") as f:
        file_data = f.read()
    # Part 1
    print(f"Answer to part 1: {determine_start_index(file_data)}")
    
    # Part 2
    print(f"Answer to part 2: {determine_start_index(file_data, 14)}")
    
