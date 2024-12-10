import os
from collections import defaultdict

file_path = os.path.join(os.path.dirname(__file__), 'input.txt')

input = open(file_path, 'r').read()

disk_map = []
spaces = defaultdict(list)
idx = block_id = 0
while idx<len(input):
    if idx % 2 == 0:
        disk_map += [str(block_id)]*int(input[idx])
        idx += 1
    else:
        spaces[block_id] = [len(disk_map), int(input[idx])]
        disk_map += ['.']*int(input[idx])
        idx += 1
        block_id += 1


for b in range(block_id, 0, -1):
    block_start = disk_map.index(str(b))
    size = disk_map.count(str(b))
    try:
        space_id = min(i for i in spaces.keys() if spaces[i][1] >= size and i < b)
        space = spaces[space_id][0]
        disk_map[space:space+size], disk_map[block_start:block_start+size] = disk_map[block_start:block_start+size], disk_map[space:space+size]
        spaces[space_id][0] += size
        spaces[space_id][1] -= size
    except ValueError:
        continue
    continue

print(sum(idx*int(val) for idx, val in enumerate(disk_map) if val != '.'))
