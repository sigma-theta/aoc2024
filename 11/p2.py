##SOLUTION TAKEN FROM https://www.youtube.com/@hyper-neutrino

import os
from functools import cache

file_path = os.path.join(os.path.dirname(__file__), 'input.txt')

input = list(map(int, open(file_path, 'r').read().strip().split(' ')))

@cache
def count(num, steps):
    if steps == 0:
        return 1
    if num == 0:
        return count(1, steps - 1)
    num_str = str(num)
    num_len = len(num_str)
    if num_len % 2 == 0:
        return count(int(num_str[:num_len // 2]), steps - 1) + count(int(num_str[num_len // 2:]), steps - 1)
    return count(num * 2024, steps - 1)

print(sum(count(i, 75) for i in input))
    
    