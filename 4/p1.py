import os
import re

file_path = os.path.join(os.path.dirname(__file__), 'input.txt')                                                                                                                                                                                             
ans = 0                          
letters = [] 
with open(file_path, 'r') as input:
    for l in input.readlines():
          letters.append([c for c in l.strip()])
# print(letters)
for i in range(len(letters)):
    #horizontal
    h_line = ''.join(letters[i])
    ans += len([match for match in re.finditer('XMAS', h_line)])
    ans += len([match for match in re.finditer('SAMX', h_line)])
transposed = [[letters[j][i] for j in range(len(letters))] for i in range(len(letters[0]))]
for i in range(len(transposed)):
    #horizontal
    v_line = ''.join(transposed[i])
    ans += len([match for match in re.finditer('XMAS', v_line)])
    ans += len([match for match in re.finditer('SAMX', v_line)])

diags1 = [[] for i in range(2*len(letters)-1)]    
diags2 = [[] for i in range(2*len(letters)-1)]    
for i in range(len(letters)):
     for j in range(len(letters[i])):
         diags1[i+j].append(letters[i][j])
         diags2[i+j].append(letters[i][len(letters[i])-1-j])
for d in diags1:
     d_line = ''.join(d)
     ans += len([match for match in re.finditer('XMAS', d_line)])
     ans += len([match for match in re.finditer('SAMX', d_line)])
for d in diags2:
     d_line = ''.join(d)
     ans += len([match for match in re.finditer('XMAS', d_line)])
     ans += len([match for match in re.finditer('SAMX', d_line)])
         
print(ans)
  
   
                   