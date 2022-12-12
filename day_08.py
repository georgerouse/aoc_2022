def is_tree_visible(orig_x, orig_y, tree_map):
    print(f"TREE POSITION x: {orig_x}, y: {orig_y}")
    current_tree_height = tree_map[orig_y][orig_x]
    forest_width = len(tree_map[0])
    forest_height = len(tree_map)
    coord_list = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    x = orig_x
    y = orig_y
    for coord in coord_list:
        still_in_forest = True
        while still_in_forest:
            # Check trees north
            x_offset = coord[0]
            y_offset = coord[1]
            x = x + x_offset
            y = y + y_offset
            
            if x < 0 or y < 0 or y >= forest_height or x >= forest_width:
                still_in_forest = False
            else:
                print(f"new_x: {x}, new_y: {y}")
                
                if tree_map[y][x] > current_tree_height:
                    return False
                    
                import pdb;pdb.set_trace()
        
        return True
               
    

with open("day_08.txt") as f:
    file = f.read()
    lines = [x for x in file.split('\n')]
    tree_map = lines = [[int(y) for y in x] for x in lines]
    width = len(tree_map[0])
    print(f"width: {width}")
    
    height = len(tree_map)
    print(f"height: {height}")
    
    for x in range(1, width-1):
        for y in range(1, height-1):
            is_tree_visible(x, y, tree_map)
    
    # Part 1
    