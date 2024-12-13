##SOLUTION TAKEN FROM https://www.youtube.com/@hyper-neutrino

import os

file_path = os.path.join(os.path.dirname(__file__), 'test.txt')

plot = []
with open(file_path, 'r') as input:
    for l in input.readlines():
        plot.append([c for c in l.strip()])
    
rows = len(plot)
cols = len(plot[0])
regions = []
seen = set()

for r in range(rows):
    for c in range(cols):
        if (r, c) in seen:
            continue
        seen.add((r, c))
        region = {(r, c)}
        to_search = [(r, c)]
        while to_search:
            cur_row, cur_col = to_search.pop(0)
            for new_row, new_col in [(cur_row - 1, cur_col), (cur_row + 1, cur_col), (cur_row, cur_col - 1), (cur_row, cur_col + 1)]:
                if new_row < 0 or new_row >= rows or new_col < 0 or new_col >= cols:
                    continue
                if plot[new_row][new_col] != plot[cur_row][cur_col]:
                    continue
                if (new_row, new_col) in region:
                    continue
                region.add((new_row, new_col))
                seen.add((new_row, new_col))
                to_search.append((new_row, new_col))
        regions.append(region)

def find_perimeter(region):
    perimeter = 0
    for sq in region:
        perimeter += 4
        for (r, c) in [(sq[0] + 1, sq[1]), (sq[0] - 1, sq[1]), (sq[0], sq[1] + 1), (sq[0], sq[1] - 1)]:
            if (r, c) in region:
                perimeter -= 1
    return perimeter

ans = 0
for reg in regions:
    ans += len(reg) * find_perimeter(reg)
print(ans)