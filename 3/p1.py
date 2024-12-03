import re
import os

file_path = os.path.join(os.path.dirname(__file__), 'input.txt')

lookup_test = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
pattern = "mul\(\s*\d+\s*,\s*\d+\s*\)"
sum = 0

with open(file_path, 'r') as input:
    for l in input.readlines():
        valid = re.findall(pattern, l)
        for i in valid:
            sum += int(i[i.find("(")+1:i.find(",")]) * int(i[i.find(",")+1:i.find(")")])
print(sum)