#SOLUTION TAKEN FROM https://www.youtube.com/@hyper-neutrino

import os

file_path = os.path.join(os.path.dirname(__file__), 'input.txt')

map = []
trailheads = []
with open(file_path, 'r') as input:
    for row, l in enumerate(input):
        map.append([int(c) for c in l.strip()])
        for col, c in enumerate(l.strip()):
            if c == '0':
                trailheads.append((row, col))

rows = len(map)
cols = len(map[0])

def bfs(grid, r, c):
    to_search = [(r, c)]
    seen = {(r, c): 1}
    paths = 0
    while len(to_search) > 0:
        cur_row, cur_col = to_search.pop(0)
        if grid[cur_row][cur_col] == 9:
            paths += seen[(cur_row, cur_col)]
        for new_row, new_col in [(cur_row - 1, cur_col), (cur_row + 1, cur_col), (cur_row, cur_col - 1), (cur_row, cur_col + 1)]:
            if new_row < 0 or new_row >= rows or new_col < 0 or new_col >= cols:
                continue
            if grid[new_row][new_col] != grid[cur_row][cur_col] + 1:
                continue
            if (new_row, new_col) in seen:
                seen[(new_row, new_col)] += seen[(cur_row, cur_col)]
                continue
            seen[(new_row, new_col)] = seen[(cur_row, cur_col)]
            to_search.append((new_row, new_col))
    return paths

ans = 0
for pos in trailheads:
    ans += bfs(map, pos[0], pos[1])
print(ans)