import os
from collections import defaultdict

file_path = os.path.join(os.path.dirname(__file__), 'input.txt')
before = defaultdict(list)
after = defaultdict(list)
ans = 0
with open(file_path, 'r') as input:
    for l in input.readlines():
        if l.find('|') > -1:
            nums = l.strip().split('|')
            b = nums[0]
            a = nums[1]
            after[b].append(a)
            before[a].append(b)
        elif l.find(',') > -1:
            nums = l.strip().split(',')
            ok = True
            for i in range(len(nums)):
                for m in nums[:i]:
                    if m in after[nums[i]]:
                        ok = False
                for n in nums[i+1:]:
                    if n in before[nums[i]]:
                        ok = False
            if not ok:
                j = 0
                while j < len(nums):
                    for m in nums[:j]:
                        if m in after[nums[j]]:
                            nums[j], nums[nums.index(m)] = nums[nums.index(m)], nums[j]
                            j = 0
                    j += 1
                ans += int(nums[len(nums)//2])
        else:
            continue
print(ans)      