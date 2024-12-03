import re
import os

file_path = os.path.join(os.path.dirname(__file__), 'input.txt')

lookup_test = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
mul_pattern = r"mul\(\d+,\d+\)"
do_pattern = r"do\(\)"
dont_pattern = r"don\'t\(\)"
sum = 0

# dont_idx = [m.start() for m in re.finditer(dont_pattern, lookup_test)]
# do_idx = [m.start() for m in re.finditer(do_pattern, lookup_test)]

# print(dont_idx)
# print(do_idx)


with open(file_path, 'r') as input:
    for l in input.readlines():
        dont_idx = [m.start() for m in re.finditer(dont_pattern, l)]
        do_idx = [m.start() for m in re.finditer(do_pattern, l)]
        # print(dont_idx)
        # print(do_idx)
        valid_parts = []
        valid_parts.append((0, dont_idx[0]))
        i = 0
        cur_invalid = dont_idx[0]
        while i < len(do_idx):
            cur_valid = do_idx[i]
            # print(f"cur valid: {cur_valid}")
            try:
                new_invalid = max(cur_invalid, [idx for idx in dont_idx if idx > cur_valid][0])
                # print(f"new invalid: {new_invalid}")
            except IndexError:
                valid_parts.append((cur_valid, len(l)))
                break
            if new_invalid != cur_invalid:
                valid_parts.append((cur_valid, new_invalid))
            cur_invalid = new_invalid
            i+=1
        # print(valid_parts)
        for p in valid_parts:
            search = l[p[0]:p[1]]
            sums = re.findall(mul_pattern, search)
            # print(sums)
            for s in sums:
                sum += int(s[s.find("(")+1:s.find(",")]) * int(s[s.find(",")+1:s.find(")")])
        # print(sum)
print(sum)
            


#dont [171, 250, 278, 1488, 2335, 2786]
#do [576, 628, 1327, 1559, 1961, 2079, 2721, 2885, 2965]
#[(0, 171), (576, 1488), (1559, 2335), (2721, 2786), (2885, 3081)]
