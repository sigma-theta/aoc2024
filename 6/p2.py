import os

file_path = os.path.join(os.path.dirname(__file__), 'input.txt')

with open(file_path, 'r') as input:
    map = [[c for c in l.strip()] for l in input.readlines()]

dirs = ['n', 'e', 's', 'w']
movements = {'n': [-1, 0], 'e': [0, 1], 's': [1, 0], 'w': [0, -1]}
ans = 0

for i in range(len(map)):
    for j in range(len(map[i])):
        # print(f'{i} {j}')
        if map[i][j] == '^' or map[i][j] == '#':
            continue
        new_map = [row[:] for row in map]
        new_map[i][j] = '#'
        seen = [(i,j) for i in range(len(new_map)) for j in range(len(new_map[i])) if new_map[i][j] == '^']
        cur_row = seen[0][0]
        cur_col = seen[0][1]
        cur_dir = dirs[0]
        while cur_row > -1 and cur_row < len(new_map) and cur_col > -1 and cur_col < len(new_map[0]):
            next_row = cur_row + movements[cur_dir][0]
            # print(f'next_row: {next_row}')
            next_col = cur_col + movements[cur_dir][1]
            # print(f'next_col: {next_col}')
            if next_row == -1 or next_row == len(new_map) or next_col == -1 or next_col == len(new_map[0]):
                cur_row = next_row
                cur_col = next_col
                continue
            if new_map[next_row][next_col] == '#':
                cur_dir = dirs[(dirs.index(cur_dir)+1)%4]
                continue
            seen.append((next_row, next_col))
            if seen.count((next_row, next_col)) > 10:
                # print(f'{i}, {j} valid')
                ans += 1
                break
            cur_row = next_row
            cur_col = next_col 
        new_map = [row[:] for row in map]
print(ans)