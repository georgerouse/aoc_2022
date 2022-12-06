import re
import copy

def convert_stacks_to_lists(stack_string_list, debug_print=False):
    stack_string_list = stack_string_list.split("\n")
    stack_height = len(stack_string_list)
    stack_len = len(stack_string_list[-1].replace(" ", "")) 
    return_list = [[] for i in range(stack_len)] # using [[]] * n makes the lists the same.... DUH!

    if debug_print:
        print(f"stack_height: {stack_height}")
        print(f"stack_len: {stack_len}")
    
    for i in range(0, stack_len):
        line_list = []
        for j in range(1, 4 * stack_height, 4):
            if j < len(stack_string_list[i]):
                # import pdb;pdb.set_trace()
                value = stack_string_list[i][j]
                if value != " ":
                    location = int((j-1)/4)
                    return_list[location].insert(0, value)
                
    if debug_print:
        print(return_list)
    return return_list
    

def apply_move(stack, move):
    # move 1 from 2 to 1
    numbers = re.findall(r'\d+', move)
    # Convert to indexes instead of stack numbers
    move_num = int(numbers[0])
    move_from = int(numbers[1]) - 1
    move_to = int(numbers[2]) - 1
    
    for i in range(move_num):
        value = stack[move_from].pop()
        stack[move_to].append(value)
    
    return stack

def apply_move_v2(stacks, move):
    # move 1 from 2 to 1
    numbers = re.findall(r'\d+', move)
    move_num = int(numbers[0])
    # Convert to indexes instead of stack numbers
    move_from = int(numbers[1]) - 1
    move_to = int(numbers[2]) - 1
    moving_list = []
    
    for i in range(move_num):
        moving_list.append(stacks[move_from].pop())
    moving_list.reverse()
    stacks[move_to] = stacks[move_to] + moving_list
    
    return stacks


def get_top_stacks(stacks):
    return_list = []
    for i in range(len(stacks)):
        return_list.append(stacks[i][-1])
    return ''.join(return_list)


if __name__ == "__main__":
    # Get the input data
    with open("inputs/day_05.txt", "r") as f:
        file_data = f.read()
    stacks, move_list = file_data.split("\n\n")
    move_list = move_list.split("\n")
    stacks = convert_stacks_to_lists(stacks)
    stacks_for_part_2 = copy.deepcopy(stacks)
    
    # Part 1
    for move in move_list:
        stacks = apply_move(stacks, move)
    part_1_answer = get_top_stacks(stacks)
    print(f"Answer to part 1: {part_1_answer}")
    
    # Part 2
    for move in move_list:
        stacks_for_part_2 = apply_move_v2(stacks_for_part_2, move)
    part_2_answer = get_top_stacks(stacks_for_part_2)
    print(f"Answer to part 2: {part_2_answer}")        
