import os

file_path = os.path.join(os.path.dirname(__file__), 'input.txt')

input = open(file_path, 'r').read().strip().split(' ')

def blink(nums, steps):
    for s in range(steps):
        new_nums = []
        for n in nums:
            if n == '0':
                new_nums.append('1')
            elif len(n) % 2 == 0:
                new_nums.append(n[:len(n)//2])
                new_nums.append(str(int(n[len(n)//2:])))
            else:
                new_nums.append(str(int(n)*2024))
        nums = new_nums
    return len(new_nums)

print(blink(input, 25))