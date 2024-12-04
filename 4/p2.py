import os
import re

file_path = os.path.join(os.path.dirname(__file__), 'input.txt')                                                                                                                                                                                             
ans = 0                          
letters = [] 
with open(file_path, 'r') as input:
    for l in input.readlines():
          letters.append([c for c in l.strip()])

for r in range(1, len(letters)-1):
    for c in range(1, len(letters[r])-1):
        if letters[r][c] != 'A':
            continue
        if letters[r-1][c-1] not in ['M','S']:
            continue
        if letters[r-1][c-1] == 'M':
            if letters[r+1][c-1] != 'M' and letters[r-1][c+1] != 'M':
                continue
            if letters[r+1][c-1] == 'M':
                if letters[r-1][c+1] != 'S' or letters[r+1][c+1] != 'S':
                    continue
                ans += 1
            if letters[r-1][c+1] == 'M':
                if letters[r+1][c-1] != 'S' or letters[r+1][c+1] != 'S':
                    continue
                ans += 1
        if letters[r-1][c-1] == 'S':
            if letters[r+1][c-1] != 'S' and letters[r-1][c+1] != 'S':
                continue
            if letters[r+1][c-1] == 'S':
                if letters[r-1][c+1] != 'M' or letters[r+1][c+1] != 'M':
                    continue
                ans += 1
            if letters[r-1][c+1] == 'S':
                if letters[r+1][c-1] != 'M' or letters[r+1][c+1] != 'M':
                    continue
                ans += 1
print(ans)
          