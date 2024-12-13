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

def find_sides(region):
    edges = {}
    for r, c in region:
        for nr, nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
            if (nr, nc) in region:
                continue
            er = (r + nr) / 2
            ec = (c + nc) / 2
            edges[(er, ec)] = (er - r, ec - c)
    seen = set()
    sides = 0
    for e, dir in edges.items():
        if e in seen:
            continue
        seen.add(e)
        sides += 1
        cr, cc = e
        if cr % 1 == 0:
            for dr in [-1, 1]:
                nr = cr + dr
                while edges.get((nr, cc)) == dir:
                    seen.add((nr, cc))
                    nr += dr
        else:
            for dc in [-1, 1]:
                nc = cc + dc
                while edges.get((cr, nc)) == dir:
                    seen.add((cr, nc))
                    nc += dc
    return sides

def find_sides_alt(region):
    maybe_corners = set()
    for r, c in region:
        for mr, mc in [(r - 0.5, c - 0.5), (r - 0.5, c + 0,5), (r + 0.5, c + 0.5), (r + 0.5, c - 0.5)]:
            maybe_corners.add((mr, mc))
    corners = 0 
    for cr, cc in maybe_corners:
        config = []
        for nr, nc in [(r - 0.5, c - 0.5), (r - 0.5, c + 0,5), (r + 0.5, c + 0.5), (r + 0.5, c - 0.5)]:
            config.append((nr, nc) in region)
        neighbors = sum(config)
        if neighbors == 1:
            corners += 1
        elif neighbors == 2:
            if config == [True, False, True, False] or config == [False, True, False, True]:
                corners += 2
        elif neighbors == 3:
            corners += 1
    return corners

print(sum(len(reg) * find_sides(reg) for reg in regions))