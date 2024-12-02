reports = []
correct = []

def check_safety(arr):
    diffs = [abs(arr[i]-arr[i+1]) for i in range(len(arr)-1)]
    if sorted(arr) != arr and sorted(arr) != arr[::-1]:
        return False
    if min(diffs) < 1 or max(diffs) > 3:
        return False
    return True

with open('input.txt', 'r') as input:
    for l in input.readlines():
        reports.append(list(map(int, l.split(' '))))

for r in reports:
    safe_removals = []
    if check_safety(r):
        correct.append(r)
        continue
    for i in range(len(r)):
        new_r = r[:]
        new_r.pop(i)
        # print(new_r)
        # print(check_safety(new_r))
        if check_safety(new_r):
            safe_removals.append(r[i])
        # print(safe_removals)
    if len(safe_removals) == 0:
        continue
    correct.append(r)

print(len(correct))
        