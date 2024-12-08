import os
from collections import defaultdict
file_path = os.path.join(os.path.dirname(__file__), 'input.txt')

def angle(point1, point2):
    if point1[0] == point2[0]:
        return 0
    if point1[1] == point2[1]:
        return 90
    else:
        return (point2[1]-point1[1])/(point2[0]-point1[0])

def is_antinode(ant1, ant2, pos):
    return angle(ant1,pos) == angle(ant2,pos)

map = []
antennas = defaultdict(list)
antinodes = []
with open(file_path, 'r') as input:
    for row, l in enumerate(input):
        map.append([c for c in l.strip()])
        for col, c in enumerate(l.strip()):
            if c != '.':
                antennas[c].append((row, col))

for ant in antennas.keys():
    if len(antennas[ant]) < 2:
        continue
    antinodes += antennas[ant]
    for i in range(len(antennas[ant])-1):
        for j in range(i+1, len(antennas[ant])): 
            for r in range(len(map)):
                for c in range(len(map[r])):
                    if is_antinode(antennas[ant][i], antennas[ant][j], (r,c)):
                        if (r,c) not in antinodes:
                            antinodes.append((r,c))
print(len(set(antinodes)))




            




