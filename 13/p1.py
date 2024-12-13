import os

file_path = os.path.join(os.path.dirname(__file__), 'input.txt')

games = []
with open(file_path, 'r') as input:
    lines = input.readlines()
    for i in range(len(lines)//4 + 1):
        game = []
        for j in range(3):
            info = lines[4*i+j].strip().split(': ')[1]
            if j == 2:
                info_x = info.split(', ')[0].split('=')[1]
                info_y = info.split(', ')[1].split('=')[1]
            else:
                info_x = info.split(', ')[0].split('+')[1]
                info_y = info.split(', ')[1].split('+')[1]
            game.append(int(info_x))
            game.append(int(info_y))
        games.append(game)

ans = 0
for g in games:
    target_x, target_y = g[-2:]
    found = []
    for i in range(101):
        for j in range(101):
            if g[0]*i + g[2]*j == target_x and g[1]*i + g[3]*j == target_y:
                found.append(3*i+j)
    if found:
        ans += min(found)

print(ans)

