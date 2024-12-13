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
                game.append(10e12+int(info_x))
                game.append(10e12+int(info_y))
            else:
                info_x = info.split(', ')[0].split('+')[1]
                info_y = info.split(', ')[1].split('+')[1]
                game.append(int(info_x))
                game.append(int(info_y))
        games.append(game)
    

ans = 0
for g in games:
    x1, y1, x2, y2, p1, p2 = g
    b = (p1*y1 - p2*x1) / (y1*x2 - x1*y2)
    a = (p1 - b*x2) / x1
    if a % 1 != 0 or b % 1 != 0:
        continue
    ans += 3*a+b

print(ans)

