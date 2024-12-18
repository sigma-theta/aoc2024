import os

file_path = os.path.join(os.path.dirname(__file__), 'input.txt')

with open(file_path, 'r') as input:
    lines = input.readlines()
    a = int(lines[0].strip().split(': ')[1])
    b = int(lines[1].strip().split(': ')[1])
    c = int(lines[2].strip().split(': ')[1])
    instructions = [int(i) for i in lines[4].strip().split(': ')[1].split(',')]

def opcode(code, op):
    global a, b, c, i, ans
    if code == 0:
        if op < 4:
            val = op 
        elif op == 4:
            val = a
        elif op == 5:
            val = b
        elif op == 6:
            val = c
        else:
            raise ValueError('invalid input')
        a = a >> val
        i += 2
    elif code == 1:
        b = b^op
        i += 2
    elif code == 2:
        if op < 4:
            val = op 
        elif op == 4:
            val = a
        elif op == 5:
            val = b
        elif op == 6:
            val = c
        else:
            raise ValueError('invalid input')
        b = val % 8
        i += 2
    elif code == 3:
        if a != 0:
            i = op
        else:
            i += 2
    elif code == 4:
        b = b^c
        i += 2
    elif code == 5:
        if op < 4:
            val = op 
        elif op == 4:
            val = a
        elif op == 5:
            val = b
        elif op == 6:
            val = c
        else:
            raise ValueError('invalid input')
        ans.append(str(val % 8))
        i += 2
    elif code == 6:
        if op < 4:
            val = op 
        elif op == 4:
            val = a
        elif op == 5:
            val = b
        elif op == 6:
            val = c
        else:
            raise ValueError('invalid input')
        b = a >> val
        i += 2
    elif code == 7:
        if op < 4:
            val = op 
        elif op == 4:
            val = a
        elif op == 5:
            val = b
        elif op == 6:
            val = c
        else:
            raise ValueError('invalid input')
        c = a >> val
        i += 2
    else:
        raise ValueError('invalid input')

i = 0
ans = []
while i < len(instructions):
    # print(i)
    opcode(instructions[i], instructions[i+1])
print(','.join(ans))