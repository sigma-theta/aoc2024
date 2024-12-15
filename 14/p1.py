import os

file_path = os.path.join(os.path.dirname(__file__), 'input.txt')

rows = 103
cols = 101
turns = 100

def find_quadrant(x, y, r ,c):
    if x == r // 2 or y == c // 2:
        return None
    elif x < r // 2:
        if y < c // 2:
            return 1
        return 2
    else:
        if y < c // 2:
            return 3
        return 4

robots = {i : 0 for i in range(1,5)}        
with open(file_path, 'r') as input:
    for l in input.readlines():
        start_y, start_x = tuple(map(int, l.strip().split(' ')[0].split('=')[1].split(',')))
        v_y, v_x = tuple(map(int, l.strip().split(' ')[1].split('=')[1].split(',')))
        fin_x = (start_x + turns * v_x) % rows
        fin_y = (start_y + turns * v_y) % cols
        # print('-'*80)
        # print(fin_x, fin_y)
        # print(find_quadrant(fin_x, fin_y, rows, cols))
        if find_quadrant(fin_x, fin_y, rows, cols):
            robots[find_quadrant(fin_x, fin_y, rows, cols)] += 1
# print(robots)

ans = 1
for v in robots.values():
    ans *= v
print(ans)