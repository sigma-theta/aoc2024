reports = []
correct = []
with open('input.txt', 'r') as input:
    for l in input.readlines():
        reports.append(list(map(int, l.split(' '))))

for r in reports:
    diffs = []
    if sorted(r) != r and sorted(r) != r[::-1]:
        continue
    for i in range(len(r)-1):
        diffs.append(abs(r[i]-r[i+1]))
    if min(diffs) < 1 or max(diffs) > 3:
        continue
    correct.append(r)

print(len(correct))
