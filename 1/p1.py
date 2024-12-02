left = []
right = []
with open('./input.txt', 'r') as input:
    for line in input.readlines():
        left.append(int(line.split('   ')[0]))
        right.append(int(line.split('   ')[1]))

print(sum(abs(x[0]-x[1]) for x in zip(sorted(left), sorted(right))))