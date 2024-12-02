left = []
right = []
sum = 0
with open('./input.txt', 'r') as input:
    for line in input.readlines():
        left.append(int(line.split('   ')[0]))
        right.append(int(line.split('   ')[1]))

for i in left:
    sum += i*right.count(i)
print(sum)
