import os 
import itertools

file_path = os.path.join(os.path.dirname(__file__), 'input.txt')

def check(vals, target, ops):
    combs = list(itertools.product(ops, repeat=len(vals)-1))
    for c in combs:
        res = 0
        # print(c)
        for i in range(len(c)):
            stmt = str(max(res,int(vals[i])))+c[i]+vals[i+1]
            # print(stmt)
            if c[i] == '|':
                res = int(str(max(res,int(vals[i])))+vals[i+1])
                continue
            res = eval(stmt)
        if res == target:
            return True
    return False
ans = 0
with open(file_path, 'r') as input:
    for l in input.readlines():
        target = int(l.strip().split(': ')[0])
        vals = l.strip().split(': ')[1].split(' ')
        # print(vals, target)
        if check(vals, target, '+*'):
            ans += target
            continue
        if check(vals, target, '+*|'):
            ans += target
            continue
print(ans)

        