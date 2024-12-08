import os 
import itertools

file_path = os.path.join(os.path.dirname(__file__), 'test.txt')

ans = 0
with open(file_path, 'r') as input:
    for l in input.readlines():
        target = int(l.strip().split(': ')[0])
        vals = l.strip().split(': ')[1].split(' ')
        # print(vals, target)
        combs = list(itertools.product('+*', repeat=len(vals)-1))
        for c in combs:
            res = 0
            # print(c)
            for i in range(len(c)):
                stmt = str(max(res,int(vals[i])))+c[i]+vals[i+1]
                # print(stmt)
                res = eval(stmt)
            # print(res)
            if res == target:
                ans+=target
                break
print(ans)

        