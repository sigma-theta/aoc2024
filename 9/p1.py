import os

file_path = os.path.join(os.path.dirname(__file__), 'input.txt')

input = open(file_path, 'r').read()

disk_map = []
idx = block_id = 0
while idx<len(input):
    if idx % 2 == 0:
        disk_map += [str(block_id)]*int(input[idx])
        idx += 1
    else:
        disk_map += ['.']*int(input[idx])
        idx += 1
        block_id += 1

blocks = [i for i in range(len(disk_map)) if disk_map[i] != '.']
spaces = [i for i in range(len(disk_map)) if disk_map[i] == '.']

while blocks[-1] > spaces[0]:
    last_block = blocks.pop()
    first_space = spaces.pop(0)
    disk_map[last_block], disk_map[first_space] = disk_map[first_space], disk_map[last_block]

print(sum(idx*int(val) for idx, val in enumerate(disk_map) if val != '.'))



